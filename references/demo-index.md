# Demo Index

本文件把 `demos/*.html` 接回优化后的任务路由。Demo 是能力演示源码和参考样例，不是 runtime 必需物，也不能替代完整流程。

## 使用原则

- 先走 `references/task-router.md` 和完整工作流，再按任务类型读对应 demo。
- Demo 只能学习结构、交互方式、验证方法和表达节奏；不要直接复制内容、数据或视觉表皮。
- 中文 demo 是默认文件名，英文 demo 带 `-en` 后缀；根据交付语言选择最近的参考。
- README 使用远程 GIF/MP4 展示效果，本地 `demos/*.html` 是源码参考。

## 路由映射

| Route | Demo files | When to read | What to learn |
|---|---|---|---|
| App prototype | `demos/c1-ios-prototype.html`, `demos/c1-ios-prototype-en.html` | 做 iOS / 移动 App 原型前 | 多屏状态管理、设备框使用、点击测试思路 |
| HTML slides / editable PPTX | `demos/c2-slides-pptx.html`, `demos/c2-slides-pptx-en.html` | 做演讲 deck 或可编辑 PPTX 前 | HTML deck 结构、PPTX 导出约束、页面 grammar |
| Motion / video | `demos/c3-motion-design.html`, `demos/c3-motion-design-en.html`, `demos/hero-animation-v10-en.html` | 做 motion、产品动画、导出 MP4/GIF 前 | Stage/Sprite 时间轴、节奏、录制准备 |
| Tweaks / variations | `demos/c4-tweaks.html`, `demos/c4-tweaks-en.html` | 需要实时调参或变体切换前 | localStorage Tweaks、参数面板、默认值设计 |
| Infographic / data viz | `demos/c5-infographic.html`, `demos/c5-infographic-en.html` | 做信息图、长图、可视化前 | 数据层级、排版密度、导出友好结构 |
| Expert critique | `demos/c6-expert-review.html`, `demos/c6-expert-review-en.html` | 用户要求 review / 打分 / 好不好看时 | 5 维评分、Keep/Fix/Quick Wins 表达 |
| Core asset protocol | `demos/w1-brand-protocol.html`, `demos/w1-brand-protocol-en.html` | 涉及具体品牌/产品时 | 问、搜、下载、验证、固化 spec 的流程展示 |
| Junior Designer workflow | `demos/w2-junior-designer.html`, `demos/w2-junior-designer-en.html` | 新任务、模糊任务、方向对齐前 | assumptions、placeholders、早展示、逐步迭代 |
| Design direction advisor | `demos/w3-fallback-advisor.html`, `demos/w3-fallback-advisor-en.html` | 没有 design context 或用户要推荐方向时 | 3 方向推荐、showcase、选择后回主流程 |

## Do Not

- 不要因为 demo 存在就跳过用户确认。
- 不要把 demo 的假数据当作真实数据。
- 不要把 demo 的风格当成默认风格；风格仍由用户 brief、品牌资产和设计方向顾问决定。

