# macOS Apps：原生架构与 Sequoia 设计指南

当用户提到「macOS 应用」「Sequoia 风格」「桌面客户端」「Mac 原型」时读这个。

## 核心哲学：内容至上，结构分明

macOS 应用不是网页的放大版，它强调**效率**和**系统一致性**。

### 1. 经典三栏/两栏架构 (Sidebar Navigation)
- **侧边栏 (Sidebar)**：应该是半透明材质 (`systemSource` 或 `vibrant-dark/light`)，图标优先使用 SF Symbols。
- **内容区 (Content)**：主操作区，通常有白色或极浅灰底色。
- **检查器 (Inspector)**：右侧辅助面板，用于显示选中项的详情。

### 2. 工具栏 (Toolbar) 演进
- **合并模式**：Sequoia 风格中，工具栏常与侧边栏标题合并，减少垂直空间浪费。
- **分段控件 (Segmented Controls)**：用于切换视图模式，不要用传统的 Tab 标签。

### 3. 材质与光效
- **材质 (Materials)**：
  - `Thick`：用于背景和侧边栏。
  - `Thin`：用于悬浮菜单或浮窗。
- **圆角 (Corner Radius)**：macOS 标准窗口圆角为 10-12px，内部组件圆角随容器逐级递减。

## 技术实现：Sequoia 视觉组件

### 1. Sidebar 玻璃材质
```css
.macos-sidebar {
  background: rgba(255, 255, 255, 0.4);
  backdrop-filter: blur(50px) saturate(190%) contrast(70%);
  border-right: 0.5px solid rgba(0, 0, 0, 0.1);
}
```

### 2. 窗口红绿灯 (Traffic Lights)
必须精确对齐：`top: 12px; left: 12px; gap: 8px;`。

## macOS 专属检查清单

- [ ] **SF Symbols**：图标是否符合苹果风格（细线条、封闭图形）？
- [ ] **交互状态**：Sidebar Item 选中态是否是全行圆角蓝色（或 Accent color）背景？
- [ ] **菜单栏考虑**：是否需要模拟 MenuBarExtra（顶部菜单栏图标）？
- [ ] **键盘快捷键**：是否在 UI 中暗示了快捷键（如 ⌘N）？

## 推荐模式：The "Pro" Interface
多面板协同。左侧导航，中间列表，右侧详情。这种结构是 macOS 生产力工具（Mail, Notes, Xcode）的灵魂。
