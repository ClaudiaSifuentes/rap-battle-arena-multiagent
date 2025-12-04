import './Header.css'

function Header() {
  return (
    <header className="header">
      <div className="header-content">
        <h1 className="header-title">
          <span className="header-icon">🎤</span>
          Rap Battle Arena
        </h1>
        <p className="header-subtitle">
          Batallas de rap 1 vs 1 con agentes especializados
        </p>
      </div>
    </header>
  )
}

export default Header

