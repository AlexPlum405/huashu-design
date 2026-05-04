# Environment Adapters

Huashu-Design should describe capabilities generically, then map them to the
current agent environment. This keeps the skill portable across Codex, Claude
Code, Cursor, OpenClaw, Hermes, and other markdown-skill agents.

## Capability Names

Use these names in workflow language:

| Capability | Meaning |
|---|---|
| `web_search` | Search the public web for current facts, official assets, specs, and release state |
| `asset_fetch` | Download or copy brand assets, product images, UI screenshots, audio, or fonts |
| `image_generation` | Generate or edit bitmap imagery when true assets are missing or variants are needed |
| `playwright_verify` | Open HTML in Chromium, capture screenshots, console warnings, page errors, and click paths |
| `design_lint` | Run static checks for assumptions, AI-slop patterns, asset references, and brand-spec usage |
| `video_render` | Render HTML animation to video/GIF and add BGM/SFX |
| `document_export` | Export HTML slides/infographics to PDF or editable PPTX |

## Codex Mapping

| Capability | Codex path |
|---|---|
| `web_search` | Use the web search tool for current facts and official sources |
| `asset_fetch` | Use shell tools such as `curl`, `yt-dlp`, `ffmpeg`, or local file reads, respecting user-provided assets |
| `image_generation` | Use the native image generation tool when available |
| `playwright_verify` | Run `python3 scripts/verify.py <html>` or `npx playwright` |
| `design_lint` | Run `python3 scripts/design_lint.py <html>` |
| `video_render` | Run `scripts/render-video.js`, `scripts/convert-formats.sh`, and `scripts/add-music.sh` |
| `document_export` | Run `scripts/export_deck_pdf.mjs`, `scripts/export_deck_stage_pdf.mjs`, or `scripts/export_deck_pptx.mjs` |

## Claude Code Mapping

| Capability | Claude Code path |
|---|---|
| `web_search` | Use WebSearch when available |
| `asset_fetch` | Use Bash / Read / Write tools; keep assets inside the project folder |
| `image_generation` | Use the environment's image model or ask for user-provided assets if unavailable |
| `playwright_verify` | Run `python3 scripts/verify.py <html>` or the local Playwright setup |
| `design_lint` | Run `python3 scripts/design_lint.py <html>` |
| `video_render` | Run the bundled video/audio scripts |
| `document_export` | Run the bundled PDF/PPTX scripts |

## Fallback Rules

- If `web_search` is unavailable, ask the user for authoritative links instead of relying on memory.
- If `image_generation` is unavailable, use official assets, public-domain/allowed assets, or honest placeholders.
- If `playwright_verify` is unavailable, open the HTML in a real browser and ask for a screenshot, but mark verification as manual.
- If `video_render` is unavailable, deliver the HTML animation and note that MP4/GIF export is pending.
- Never silently skip a capability that is required by the route table. State the missing capability and choose the safest fallback.

