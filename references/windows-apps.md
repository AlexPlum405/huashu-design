# Windows 11 Apps：Fluent Design 与 Mica 材质指南

当用户提到「Windows 应用」「Win11 风格」「Fluent Design」「Mica 效果」时读这个。

## 核心哲学：开放、现代、沉浸感

Windows 11 的 Fluent Design 强调材质的层次感和排版的呼吸感。

### 1. Mica 与 Acrylic 材质
- **Mica (云母)**：用于主窗口背景。它不是简单的半透明，而是根据桌面壁纸生成的非透明材质，不随窗口移动而重绘（性能优化）。
- **Acrylic (亚克力)**：用于临时表面（菜单、浮窗）。强调深层模糊。

### 2. 导航模式
- **侧边导航 (Navigation Rail/View)**：Win11 标准。图标通常较厚（Segoe Fluent Icons），背景在选中时有微妙的指示条。
- **居中对齐**：Win11 倾向于平衡。标题栏有时居中，主要动作在 Command Bar 中。

### 3. 字体与间距
- **Segoe UI Variable**：标准字体。在不同字号下有不同的光学校准。
- **大圆角**：窗口圆角为 8px（比起 macOS 的 12px 稍小且硬朗）。

## 技术实现：Fluent UI 核心组件

### 1. Mica 效果模拟
```css
.windows-mica {
  background: rgba(243, 243, 243, 0.85); /* 模拟灰白色 Mica */
  backdrop-filter: blur(60px) saturate(150%);
}
```

### 2. 标准按钮
Win11 按钮在 Hover 时会有微妙的边框高亮或背景加深。

## Windows 专属检查清单

- [ ] **Snap Layouts**：设计是否考虑了在不同分屏比例下的自适应？
- [ ] **Segoe Fluent Icons**：图标是否符合微软风格（等粗线条、圆角末端）？
- [ ] **交互动效**：按钮点击时是否有「向内按下」的压缩动效？
- [ ] **暗色模式适配**：Win11 的暗色 Mica (Dark Mica) 质感非常重，背景通常为 `#1C1C1C` 左右。

## 推荐模式：The "Utility" Interface
高密度工具栏配合清晰的数据表格。Win11 擅长处理信息密集的「生产力仪表盘」，通过层级清晰的标题和卡片将数据分类。
