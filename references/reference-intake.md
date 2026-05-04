# Reference Intake Protocol

Reference Intake 是自动优先、失败可跳过的参考采样步骤。它发生在事实验证 / 品牌资产协议之后，设计方向顾问或 Junior pass 之前。

## Position in Workflow

```text
任务路由
→ 事实验证
→ 品牌 / 产品资产采集
→ Reference Intake 自动采样
→ 设计 brief
→ 3 个设计方向
→ Junior pass
→ Full pass
→ lint / verify
```

## Default Behavior

1. 根据 `references/task-router.md` 的 route 和 `references/inspiration-sources.md` 的默认来源，自动尝试采样。
2. 只读取公开页面、搜索结果摘要、官网说明、用户提供的链接或截图。
3. 不绕登录、不访问付费内容、不批量下载图片。
4. 采样结果写入项目的 `reference-board.md`。
5. 任一来源不可访问时，只提示用户一句，并继续流程。

## Failure Message

当来源不可访问、需要登录、需要订阅或反爬阻断时，用一句话提示：

```text
Mobbin / Pageflows 部分内容需要登录或不可自动读取。你可以手动发截图/链接，也可以跳过；我会用已有公开参考继续。
```

不要反复追问，不要让这一步阻塞完整流程。

## `reference-board.md` Template

```markdown
# Reference Board
> Created: YYYY-MM-DD
> Route: <web / app / motion / ...>
> Status: <complete / partial / skipped>

## Sources attempted
- <Source>: <accessible / summary-only / login-required / unavailable>

## Patterns extracted
- Layout: <what structure can be learned>
- Hierarchy: <what information priority can be learned>
- Interaction: <what flow or state behavior can be learned>
- Visual tone: <what mood or design temperature can be learned>

## Applied to this project
- <How the extracted pattern informs the 3 directions or Junior pass>

## Do not copy
- No screenshots, copied UI, copied copy, copied brand assets, or paid/login-only content.
```

## When to Skip

- User explicitly says not to use external references.
- Task is a narrow edit to an existing design and reference intake would add noise.
- No public sources are reachable and user chooses not to provide screenshots.
- High urgency: do a compressed intake from existing context only, but still record `reference-board.md` as `skipped`.

## Quality Rules

- A reference is useful only if it changes layout, hierarchy, density, interaction, motion, or tone decisions.
- If it only adds decoration, do not use it.
- `reference-board.md` is evidence for direction, not a gallery.

