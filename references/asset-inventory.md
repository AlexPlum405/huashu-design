# Asset Inventory

本文件记录容易被静态引用检查误判的资产。清理前先看这里。

## Keep

| Asset | Status | Used by | Keep reason | Cleanup rule |
|---|---|---|---|---|
| `demos/*.html` | keep-source | `references/demo-index.md`, README demo gallery context | 能力演示源码和设计参考，不是 runtime 必需物 | 源码仓库保留；发布 runtime 包可选择排除 |
| `assets/bgm-educational-alt.mp3` | keep-dynamic | `scripts/add-music.sh --mood=educational-alt` | BGM mood 动态依赖，静态 grep 不一定能发现 | 只有删除对应 mood 支持时才能删除 |
| `assets/bgm-tutorial-alt.mp3` | keep-dynamic | `scripts/add-music.sh --mood=tutorial-alt` | BGM mood 动态依赖，静态 grep 不一定能发现 | 只有删除对应 mood 支持时才能删除 |
| `assets/macos_window.jsx` | keep-routed | `references/task-router.md` desktop route | 桌面 App / macOS mockup starter component | 只有移除桌面 App 路由时才能删除 |
| `references/cinematic-patterns.md` | keep-routed | `references/task-router.md` motion route | 复杂叙事动画 / cinematic demo 参考 | 只有 motion route 不再支持 cinematic 场景时才能删除 |

## Removed

| Asset | Removed because | Verification |
|---|---|---|
| `assets/banner.svg` | 仓库内无引用，也未发现发布/marketplace 配置约定 | `rg "banner\\.svg|assets/banner"` 无结果 |

## Cleanup Policy

- `keep-dynamic` 资产不能只靠静态 grep 删除。
- `keep-source` 资产可以从发布包排除，但源码仓库保留。
- `external-candidate` 资产必须先确认外部平台约定，再决定删除。
- 删除资产后必须更新本文件的 `Removed` 表。

