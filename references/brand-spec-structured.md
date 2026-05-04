# Structured Brand Spec

Huashu-Design stores brand work in two files:

- `brand-spec.md` for human-readable reasoning, sources, quality notes, and usage rules.
- `brand-spec.json` for machine-readable asset paths, colors, fonts, and constraints.

Both files are required whenever the core asset protocol is triggered.

## `brand-spec.md`

```markdown
# <Brand> · Brand Spec
> 采集日期：YYYY-MM-DD
> 资产来源：<列出下载来源>
> 资产完整度：<完整 / 部分 / 推断>

## 核心资产

### Logo
- 主版本：`assets/<brand>-brand/logo.svg`
- 浅底反色版：`assets/<brand>-brand/logo-white.svg`
- 使用场景：<片头/片尾/角落水印/全局>
- 禁用变形：<不能拉伸/改色/加描边>

### 产品图（实体产品必填）
- 主视角：`assets/<brand>-brand/product-hero.png`
- 细节图：`assets/<brand>-brand/product-detail-1.png`
- 场景图：`assets/<brand>-brand/product-scene.png`

### UI 截图（数字产品必填）
- 主页：`assets/<brand>-brand/ui-home.png`
- 核心功能：`assets/<brand>-brand/ui-feature-<name>.png`

## 辅助资产

### 色板
- Primary: #XXXXXX
- Background: #XXXXXX
- Ink: #XXXXXX
- Accent: #XXXXXX
- 禁用色: <品牌明确不用的色系>

### 字型
- Display: <font stack>
- Body: <font stack>
- Mono: <font stack>

### 签名细节
- <哪些细节是 120% 做到的>

### 禁区
- <明确不能做的>

### 气质关键词
- <3-5 个形容词>
```

## `brand-spec.json`

```json
{
  "brand": "<Brand>",
  "collectedAt": "YYYY-MM-DD",
  "sourceCompleteness": "complete | partial | inferred",
  "sources": [
    {
      "label": "Official brand page",
      "url": "https://example.com/brand",
      "usedFor": ["logo", "colors"]
    }
  ],
  "assets": {
    "logo": {
      "primary": "assets/<brand>-brand/logo.svg",
      "inverse": "assets/<brand>-brand/logo-white.svg"
    },
    "product": {
      "hero": "assets/<brand>-brand/product-hero.png",
      "details": ["assets/<brand>-brand/product-detail-1.png"],
      "scenes": []
    },
    "ui": {
      "home": "assets/<brand>-brand/ui-home.png",
      "features": []
    }
  },
  "colors": {
    "primary": "#XXXXXX",
    "background": "#XXXXXX",
    "ink": "#XXXXXX",
    "accent": "#XXXXXX",
    "forbidden": []
  },
  "fonts": {
    "display": "<font stack>",
    "body": "<font stack>",
    "mono": "<font stack>"
  },
  "signatureDetails": [],
  "avoid": [],
  "keywords": []
}
```

## Usage Rules

- HTML references assets from `brand-spec.json`, not from memory.
- CSS variables are injected from `brand-spec.json`: `--brand-primary`, `--brand-bg`, `--brand-ink`, `--brand-accent`.
- Logo and product images are real `<img>` assets. Do not redraw them with CSS or SVG.
- Run `scripts/design_lint.py <html> --brand-spec brand-spec.json` before delivery.

