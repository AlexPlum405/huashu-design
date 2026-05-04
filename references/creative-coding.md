# Creative Coding：数学艺术与粒子系统指南

当用户提到「生成艺术」「粒子效果」「酷炫背景」「数学之美」「Shader 质感」时读这个。

## 核心哲学：用代码绘画

Creative Coding 不追求像素级的布局精准，而追求**规律中的随机性 (Controlled Randomness)** 和**动态的生命力**。

### 1. 规律中的随机 (Noise & Random)
- **避免纯随机**：`Math.random()` 会让效果看起来很乱。使用正弦波 (`Math.sin`) 或柏林噪声 (Perlin Noise) 来创建自然的过渡。
- **参数化控制**：将速度、大小、颜色、数量等变量暴露出来，通过 `tweaks-system.md` 进行实时调优。

### 2. 粒子与场 (Particles & Fields)
- **个体行为**：每个粒子应该有自己的位置、速度、加速度和寿命。
- **群体交互**：粒子之间可以有引力、斥力，或者受全局“风”的影响。
- **性能红线**：在 Canvas 中处理 1000-5000 个粒子是安全的。超过 1 万个请考虑 WebGL 或精简算法。

### 3. 视觉反馈 (Visual Feedback)
- **拖尾效应 (Trailing)**：不要每帧清空画布，而是覆盖一层极淡的底色（如 `rgba(0,0,0,0.05)`），创造出流星般的拖尾效果。
- **发光感 (Glow)**：使用 `ctx.shadowBlur` 或叠加混合模式 (`ctx.globalCompositeOperation = 'screen'`) 实现发光质感。

## 技术实现：Canvas 起手式

```javascript
const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

function animate() {
  // 1. 拖尾清空
  ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  
  // 2. 更新逻辑
  particles.forEach(p => p.update());
  
  // 3. 绘制逻辑
  particles.forEach(p => p.draw(ctx));
  
  requestAnimationFrame(animate);
}
```

## Creative Coding 专属检查清单

- [ ] **高分屏适配**：是否处理了 `devicePixelRatio` 以防止 Canvas 模糊？
- [ ] **窗口自适应**：监听 `resize` 事件并重新初始化或缩放 Canvas。
- [ ] **性能监控**：在复杂效果中打开 `stats.js` 查看 FPS。
- [ ] **交互响应**：粒子是否会对鼠标位置产生反应（吸引或排斥）？

## 推荐模式：Mathematical Geometry

利用简单的几何图形（圆、线）配合正弦波动画，创建具有节奏感的视觉艺术。这种风格非常适合作为 AI 产品或科技产品的背景。
