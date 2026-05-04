# Spatial UI：空间计算与 3D 设计指南

当用户提到「Spatial UI」「Vision Pro 风格」「3D 原型」「空间计算」时读这个。

## 核心哲学：从 2D 画布到 3D 场域

Spatial UI 不仅仅是把 2D 窗口悬浮在空中。它的核心在于**深度 (Depth)**、**材质 (Material)** 和**物理感 (Physicality)**。

### 1. Z-Axis 才是主角
- **深度暗示**：不只是层级，而是真实的 Z 轴位移。背景、窗口、悬浮控制项之间应该有明确的距离感。
- **视觉锚点**：在无边界的空间中，需要一个视觉中心或地平面来锚定用户的视线。

### 2. 玻璃拟态 (Glassmorphism) v2
- **自适应光照**：玻璃材质不应是死板的 `rgba(255,255,255,0.2)`，而应该通过 `backdrop-filter: blur(20px) saturate(180%)` 实现。
- **镜面高光**：边缘增加 `1px solid rgba(255,255,255,0.3)` 的描边，模拟光线在玻璃边缘的折射。

### 3. 视差与凝视反馈 (Parallax & Gaze)
- **多层视差**：当用户移动或滑动时，内容物应以不同速度位移，强化深度感。
- **高亮反馈**：模拟 Vision Pro 的凝视高光（Gaze feedback），当鼠标经过或聚焦时，元素应有微妙的 scale 提升或材质亮度增加。

## 技术实现：CSS 3D 魔法

不要轻易上 Three.js（除非是极其复杂的 3D 模型）。CSS 3D 对于 Spatial UI 原型来说性能更好、开发更轻。

### 1. 场景配置
```css
.spatial-scene {
  perspective: 1200px;
  transform-style: preserve-3d;
}
```

### 2. 窗口悬浮
```css
.glass-window {
  transform: translateZ(50px) rotateY(-5deg);
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 40px 100px rgba(0,0,0,0.3);
}
```

## Spatial UI 专属检查清单

- [ ] **阴影跟随**：悬浮窗是否在“地面”或其他表面投射了阴影？（用 `filter: drop-shadow`）
- [ ] **视角中心**：是否处理了 `perspective-origin`？默认在中心，侧视时需要调整。
- [ ] **交互深度**：按钮按下时，是否真的在 Z 轴上向内移动了（`translateZ(-10px)`）？
- [ ] **环境沉浸**：是否有合适的背景图片（全景图或极淡的渐变）来模拟现实物理环境？

## 推荐模式：Floating Stack

将多个 2D 组件在 Z 轴上排列，形成一个具有深度的信息堆栈。最核心的信息在最前面（Z=100），辅助信息在后面（Z=0），形成自然的视觉关注顺序。
