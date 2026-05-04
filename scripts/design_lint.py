#!/usr/bin/env python3
"""
design_lint.py - Static checks for Huashu-Design HTML outputs.

This script does not replace visual review. It catches common AI-slop and
workflow violations before Playwright verification:

    python scripts/design_lint.py path/to/design.html
    python scripts/design_lint.py path/to/design.html --brand-spec brand-spec.json
    python scripts/design_lint.py path/to/design.html --strict
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Finding:
    level: str
    code: str
    message: str
    line: int | None = None


SLOP_GRADIENT_RE = re.compile(
    r"(linear-gradient|radial-gradient|conic-gradient)\([^)]*(#[0-9a-fA-F]{6}|purple|violet|indigo|blue|cyan)",
    re.IGNORECASE,
)
HEX_RE = re.compile(r"#[0-9a-fA-F]{6}\b")
EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002700-\U000027BF\U00002600-\U000026FF]"
)
FONT_RE = re.compile(r"font-family\s*:\s*([^;}\n]+)", re.IGNORECASE)
DISPLAY_CLASS_RE = re.compile(r"(hero|headline|display|title|masthead|cover)", re.IGNORECASE)
STAT_RE = re.compile(r"\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\s*(?:%|x|X|ms|s|k|K|M|B)\b")


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def add_regex_findings(findings: list[Finding], text: str, regex: re.Pattern, code: str, message: str, level: str = "warn") -> None:
    for match in regex.finditer(text):
        findings.append(Finding(level, code, message, line_number(text, match.start())))


def load_brand_spec(path: Path | None) -> dict | None:
    if path is None:
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return {"__error__": str(exc)}


def has_assumptions_block(text: str) -> bool:
    lower = text.lower()
    return (
        "assumptions" in lower
        or "我的假设" in text
        or "design decisions" in lower
        or "reasoning" in lower
    )


def check_font_slop(text: str, findings: list[Finding]) -> None:
    for match in FONT_RE.finditer(text):
        value = match.group(1).lower()
        open_brace = text.rfind("{", 0, match.start())
        close_brace = text.rfind("}", 0, match.start())
        nearby = text[close_brace + 1:open_brace] if open_brace > close_brace else ""
        if any(font in value for font in ("inter", "roboto", "arial", "system-ui", "-apple-system")):
            if DISPLAY_CLASS_RE.search(nearby):
                findings.append(
                    Finding(
                        "warn",
                        "FONT_DISPLAY_GENERIC",
                        "Generic system font appears near display/hero/title styling. Use brand font or a deliberate display/body pairing.",
                        line_number(text, match.start()),
                    )
                )


def check_large_radius(text: str, findings: list[Finding]) -> None:
    for match in re.finditer(r"border-radius\s*:\s*(\d+(?:\.\d+)?)px", text, re.IGNORECASE):
        value = float(match.group(1))
        if value >= 24:
            findings.append(
                Finding(
                    "warn",
                    "RADIUS_LARGE",
                    "Large border radius can drift into generic card UI. Keep it only when the brand/system calls for it.",
                    line_number(text, match.start()),
                )
            )


def check_left_accent_cards(text: str, findings: list[Finding]) -> None:
    pattern = re.compile(r"border-left\s*:\s*[^;]+(#[0-9a-fA-F]{3,6}|var\()", re.IGNORECASE)
    add_regex_findings(
        findings,
        text,
        pattern,
        "LEFT_ACCENT_CARD",
        "Colored left-border accents are a common AI-slop card pattern. Keep only if it is part of the design system.",
    )


def check_fake_stats(text: str, findings: list[Finding]) -> None:
    stats = STAT_RE.findall(text)
    if len(stats) >= 6 and not any(token in text.lower() for token in ("source:", "来源", "data-source", "placeholder")):
        findings.append(
            Finding(
                "warn",
                "UNSOURCED_STATS",
                "Many numeric claims found without visible source/placeholder labeling. Avoid decorative fake stats.",
            )
        )


def check_brand_spec_usage(text: str, html_path: Path, brand_spec: dict | None, findings: list[Finding]) -> None:
    if brand_spec is None:
        return
    if "__error__" in brand_spec:
        findings.append(Finding("error", "BRAND_SPEC_INVALID", f"Cannot parse brand spec: {brand_spec['__error__']}"))
        return

    assets = brand_spec.get("assets", {})
    logos = assets.get("logo", {}) if isinstance(assets, dict) else {}
    logo_paths = [p for p in logos.values() if isinstance(p, str) and p]
    if logo_paths and not any(Path(p).name in text or p in text for p in logo_paths):
        findings.append(Finding("error", "LOGO_NOT_REFERENCED", "brand-spec.json defines a logo but HTML does not reference it."))

    colors = brand_spec.get("colors", {})
    allowed = {str(v).lower() for v in colors.values() if isinstance(v, str) and HEX_RE.fullmatch(v)}
    html_hex = {m.group(0).lower() for m in HEX_RE.finditer(text)}
    stray = sorted(html_hex - allowed - {"#000000", "#ffffff", "#f5f5f5", "#fafafa", "#111111", "#1a1a1a"})
    if allowed and len(stray) > 8:
        findings.append(
            Finding(
                "warn",
                "MANY_STRAY_COLORS",
                f"HTML uses many colors outside brand-spec.json ({len(stray)} found). Route colors through CSS variables.",
            )
        )

    spec_name = html_path.parent / "brand-spec.json"
    if not spec_name.exists():
        findings.append(Finding("warn", "BRAND_SPEC_NOT_COLOCATED", "brand-spec.json is not next to the HTML output."))


def lint_html(html_path: Path, brand_spec_path: Path | None = None) -> list[Finding]:
    text = html_path.read_text(encoding="utf-8", errors="replace")
    findings: list[Finding] = []

    if not has_assumptions_block(text):
        findings.append(
            Finding(
                "error",
                "MISSING_ASSUMPTIONS",
                "HTML should begin with assumptions/reasoning/placeholders from the Junior Designer pass.",
            )
        )

    lower = text.lower()
    has_honest_placeholder = "placeholder" in lower or "待补" in text or "占位" in text
    if "<img" not in lower and not has_honest_placeholder and any(token in lower for token in ("brand", "logo", "product", "官网", "产品", "品牌")):
        findings.append(
            Finding(
                "error",
                "NO_REAL_IMAGES",
                "Brand/product-oriented output mentions brand/product but has no <img>. Use real assets or honest placeholders.",
            )
        )

    add_regex_findings(
        findings,
        text,
        SLOP_GRADIENT_RE,
        "GENERIC_GRADIENT",
        "Purple/blue/cyan gradient detected. Use only if brand-spec explicitly supports it.",
    )
    add_regex_findings(
        findings,
        text,
        EMOJI_RE,
        "EMOJI_ICON",
        "Emoji detected. Avoid emoji as iconography unless it is part of the brand tone.",
    )
    check_font_slop(text, findings)
    check_large_radius(text, findings)
    check_left_accent_cards(text, findings)
    check_fake_stats(text, findings)
    check_brand_spec_usage(text, html_path, load_brand_spec(brand_spec_path), findings)

    return findings


def print_report(findings: list[Finding], html_path: Path) -> None:
    print(f"Design lint: {html_path}")
    if not findings:
        print("OK: no findings")
        return
    for finding in findings:
        loc = f":{finding.line}" if finding.line else ""
        print(f"{finding.level.upper()} {finding.code}{loc} - {finding.message}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint Huashu-Design HTML output for workflow and AI-slop risks.")
    parser.add_argument("html_path", help="HTML file to lint")
    parser.add_argument("--brand-spec", default=None, help="Optional brand-spec.json path")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    html_path = Path(args.html_path).resolve()
    if not html_path.exists():
        print(f"ERROR: file not found: {html_path}", file=sys.stderr)
        return 2

    brand_spec_path = Path(args.brand_spec).resolve() if args.brand_spec else None
    findings = lint_html(html_path, brand_spec_path)
    print_report(findings, html_path)

    has_error = any(f.level == "error" for f in findings)
    has_warning = any(f.level == "warn" for f in findings)
    if has_error or (args.strict and has_warning):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
