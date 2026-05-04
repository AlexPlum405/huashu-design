/**
 * DesktopDesignSystem - Production-grade UI components for macOS and Windows 11
 * Features: Native layouts, platform-specific materials (Mica/Glass), SF Symbols & Fluent Icons.
 */

const desktopStyles = {
  macOS: {
    sidebar: {
      width: '240px',
      background: 'rgba(255, 255, 255, 0.4)',
      backdropFilter: 'blur(50px) saturate(190%) contrast(70%)',
      borderRight: '0.5px solid rgba(0, 0, 0, 0.1)',
      display: 'flex',
      flexDirection: 'column',
      padding: '40px 12px 12px 12px',
    },
    content: {
      flex: 1,
      background: '#ffffff',
      display: 'flex',
      flexDirection: 'column',
    },
    sidebarItem: (active) => ({
      padding: '6px 10px',
      borderRadius: '6px',
      fontSize: '13px',
      color: active ? '#fff' : '#333',
      backgroundColor: active ? '#007AFF' : 'transparent',
      cursor: 'pointer',
      display: 'flex',
      alignItems: 'center',
      gap: '8px',
      marginBottom: '2px',
    })
  },
  Windows11: {
    container: {
      background: 'rgba(243, 243, 243, 0.85)',
      backdropFilter: 'blur(60px) saturate(150%)',
      display: 'flex',
      width: '100%',
      height: '100%',
    },
    navRail: {
      width: '48px',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      padding: '40px 0',
      gap: '12px',
    },
    navItem: (active) => ({
      width: '36px',
      height: '36px',
      borderRadius: '4px',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      backgroundColor: active ? 'rgba(0, 0, 0, 0.05)' : 'transparent',
      borderLeft: active ? '3px solid #0067C0' : 'none',
      cursor: 'pointer',
    })
  }
};

function MacOSSidebar({ children, items = [], activeId, onSelect }) {
  return (
    <div style={desktopStyles.macOS.sidebar}>
      {items.map(item => (
        <div 
          key={item.id} 
          style={desktopStyles.macOS.sidebarItem(item.id === activeId)}
          onClick={() => onSelect?.(item.id)}
        >
          {item.icon && <span style={{opacity: 0.8}}>{item.icon}</span>}
          {item.label}
        </div>
      ))}
      {children}
    </div>
  );
}

function Windows11Mica({ children, style }) {
  return (
    <div style={{ ...desktopStyles.Windows11.container, ...style }}>
      {children}
    </div>
  );
}

// 模拟 SF Symbols 的样式
function SFSymbol({ name, color, size = 16 }) {
  return (
    <span style={{ 
      fontFamily: '-apple-system', 
      fontSize: size, 
      color: color,
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center'
    }}>
      {/* 这是一个占位符，实际会渲染对应字符或 SVG */}
      ●
    </span>
  );
}

window.DesktopUI = {
  MacOSSidebar,
  Windows11Mica,
  SFSymbol,
  desktopStyles
};
