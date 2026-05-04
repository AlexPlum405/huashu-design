# Task Router and Definition of Done

This file is the first routing layer for Huashu-Design work. It does not weaken
the main workflow. It makes the full workflow easier to execute consistently.

## Forced Execution Contract

Huashu-Design exists to help users steer design direction. It must not turn a
single vague prompt into a polished final artifact without direction alignment.

Hard rules:

- Do not write final HTML / slides / animation / prototype immediately from a vague prompt.
- Do not use "I'll make one first" to bypass questions, asset checks, direction restatement, or the Junior Designer pass.
- Do not downgrade checkpoint gates into optional notes. When a checkpoint appears, stop and wait for confirmation.
- If the user says "just do it", use the compressed full workflow: assumptions, 3 directions, critical risks, confirmation, then Full pass.

## Route Table

| User intent / keywords | Output type | Required references | Reference intake defaults | Required assets / scripts | Demo reference | Done when |
|---|---|---|---|---|---|---|
| 页面、官网、landing、Web mockup、开发文档 | Web page / web prototype | `references/workflow.md` + `references/design-context.md` + `references/content-guidelines.md` | Awwwards, Behance, Dribbble | `assets/browser_window.jsx` when browser chrome is useful + `scripts/design_lint.py` + `scripts/verify.py` | `references/demo-index.md` if a nearby web demo exists | 3 directions aligned + HTML + at least 2 viewport screenshots + lint pass or explained warnings |
| App、iOS、Android、移动端、可点击流程 | App prototype | `references/workflow.md` + App/iOS rules in `SKILL.md` + `references/react-setup.md` | Mobbin, UI Pocket, Pageflows | `assets/ios_frame.jsx` or `assets/android_frame.jsx` + `scripts/verify.py` + click test | `demos/c1-ios-prototype*.html` | Overview/flow shape confirmed + real imagery or honest placeholders + key click path verified |
| 桌面 App、macOS mockup、desktop prototype | Desktop app prototype | `references/workflow.md` + `references/design-context.md` + `references/react-setup.md` | Pageflows, Behance, relevant product docs | `assets/macos_window.jsx` + `scripts/design_lint.py` + `scripts/verify.py` | `references/demo-index.md` for workflow pattern; no dedicated desktop demo yet | Window chrome confirmed + primary workflow visible + screenshot verification |
| PPT、幻灯片、deck、演讲 | HTML slides | `references/slide-decks.md` + `references/editable-pptx.md` only for editable PPTX | Behance, Awwwards, existing deck references | `assets/deck_index.html` or `assets/deck_stage.js` + export scripts | `demos/c2-slides-pptx*.html` | 2-page showcase grammar + HTML aggregate version + per-slide screenshots |
| 动画、motion、发布视频、导出 MP4/GIF | Motion / video | `references/animation-pitfalls.md` + `references/animation-best-practices.md` + `references/cinematic-patterns.md` + `references/video-export.md` | Pageflows, Design Spells, Awwwards motion-heavy sites | `assets/animations.jsx` + `scripts/render-video.js` + `scripts/add-music.sh` | `demos/c3-motion-design*.html` + `demos/hero-animation-v10-en.html` | Timeline stated + HTML animation + MP4/GIF with default BGM/SFX + audio stream checked |
| Spatial UI、Vision Pro、3D 原型、空间计算 | Spatial Prototype | `references/spatial-ui.md` + `references/react-setup.md` | Apple Spatial Design, Behance (Spatial UI) | `assets/spatial_canvas.jsx` + `scripts/verify.py` | - | 3D scene aligned + glassmorphism used + depth layers confirmed |
| 粒子、生成艺术、创意编程、Canvas 动画、粒子背景 | Creative Coding | `references/creative-coding.md` + `references/tweaks-system.md` | uiverse, Dribbble, Codepen | `assets/particles_engine.jsx` + `scripts/design_lint.py` | - | Dynamic parameters exposed + Canvas performance pass + mathematical logic confirmed |
| 信息图、可视化、PDF、长图 | Infographic / visualization | `references/scene-templates.md` + `references/content-guidelines.md` + `references/verification.md` | Behance, Awwwards, scene templates | `scripts/design_lint.py` + `scripts/verify.py` | `demos/c5-infographic*.html` | Layout direction confirmed + data source/placeholder labels + screenshot/export |
| Tweaks、调参、变体切换 | Tweaks / interactive variations | `references/tweaks-system.md` + `references/workflow.md` | uiverse, Dribbble, Design Spells | `assets/design_canvas.jsx` or localStorage Tweaks + `scripts/design_lint.py` + `scripts/verify.py` | `demos/c4-tweaks*.html` | Default design complete + meaningful tweak set + persisted state verified |
| 评审、好不好看、review、打分 | Expert review | `references/critique-guide.md` | User artifact first; closest route if needed | Optional `scripts/verify.py` screenshots as evidence | `demos/c6-expert-review*.html` | 5-dimension score + Keep/Fix/Quick Wins; do not edit unless user asks |

## Supporting Indexes

- Demo mapping: `references/demo-index.md`
- Asset retention / cleanup rules: `references/asset-inventory.md`
- Inspiration sources: `references/inspiration-sources.md`
- Reference intake protocol: `references/reference-intake.md`

## Universal Definition of Done

Every design artifact must satisfy these before final delivery:

- Fact verification is complete when concrete products, technologies, events, people, specs, or launch state are involved.
- Design context, brand assets, and direction checkpoints are complete. If no context exists, design advisor fallback was used.
- Reference Intake has been attempted or explicitly skipped, with `reference-board.md` recorded when useful.
- The HTML artifact includes assumptions, reasoning, and placeholders, or states that they were confirmed and replaced.
- There are at least two meaningful variations, or the response explains why the task can only support one.
- `scripts/design_lint.py <html>` has been run. Warnings are either fixed or explained.
- Playwright / `scripts/verify.py` screenshot verification has been run with no page errors.
- Final summary is short and limited to caveats and next steps.
