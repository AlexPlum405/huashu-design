/**
 * SpatialCanvas - A lightweight React wrapper for Spatial UI & 3D Prototypes
 * Principles: 3D perspective, glassmorphism, gaze feedback.
 */

const spatialStyles = {
  scene: {
    perspective: '1200px',
    transformStyle: 'preserve-3d',
    width: '100vw',
    height: '100vh',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    overflow: 'hidden',
    background: 'radial-gradient(circle at center, #2a2a2a, #000)',
    color: '#fff',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
  },
  glass: {
    background: 'rgba(255, 255, 255, 0.05)',
    backdropFilter: 'blur(25px) saturate(150%)',
    borderRadius: '24px',
    border: '1px solid rgba(255, 255, 255, 0.15)',
    boxShadow: '0 40px 100px rgba(0, 0, 0, 0.4)',
    padding: '24px',
    transformStyle: 'preserve-3d',
    transition: 'transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1)',
  },
  gaze: {
    cursor: 'pointer',
    transition: 'all 0.3s ease',
  }
};

function SpatialScene({ children, style, ...props }) {
  return (
    <div style={{ ...spatialStyles.scene, ...style }} {...props}>
      {children}
    </div>
  );
}

function FloatingWindow({ children, z = 0, rx = 0, ry = 0, style, ...props }) {
  return (
    <div 
      style={{ 
        ...spatialStyles.glass, 
        transform: `translateZ(${z}px) rotateX(${rx}deg) rotateY(${ry}deg)`,
        ...style 
      }} 
      {...props}
    >
      {children}
    </div>
  );
}

function GazeElement({ children, style, activeScale = 1.05, activeBrightness = 1.2, ...props }) {
  const [isHovered, setIsHovered] = React.useState(false);
  
  return (
    <div
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      style={{
        ...spatialStyles.gaze,
        transform: isHovered ? `scale(${activeScale}) translateZ(10px)` : 'scale(1)',
        filter: isHovered ? `brightness(${activeBrightness})` : 'brightness(1)',
        ...style
      }}
      {...props}
    >
      {children}
    </div>
  );
}

window.SpatialUI = {
  SpatialScene,
  FloatingWindow,
  GazeElement,
  spatialStyles
};
