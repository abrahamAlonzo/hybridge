import { useState } from 'react'
import './App.css'
import SearchBar from './components/SearchBar'
import Button from './components/Button'

function App() {
  const [searchQuery, setSearchQuery] = useState('')

  const handleSearch = (e) => {
    e.preventDefault()
    if (searchQuery.trim()) {
      const query = encodeURIComponent(searchQuery)
      window.location.href = `https://www.google.com/search?q=${query}`
    }
  }

  const handleLucky = () => {
    if (searchQuery.trim()) {
      const query = encodeURIComponent(searchQuery)
      window.location.href = `https://www.google.com/search?q=${query}`
    }
  }

  return (
    <div className="app">
      <header className="header">
        <nav className="nav">
          <a href="https://mail.google.com" target="_blank" className="nav-link">Gmail</a>
          <a href="https://www.google.com/imghp" target="_blank" className="nav-link">Imágenes</a>
          <div className="menu-icon">
            <svg viewBox="0 0 24 24">
              <path d="M6,8c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM12,20c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM6,20c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM6,14c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM12,14c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM16,6c0,1.1 0.9,2 2,2s2,-0.9 2,-2 -0.9,-2 -2,-2 -2,0.9 -2,2zM12,8c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM18,14c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM18,20c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2z"></path>
            </svg>
          </div>
          <div className="user-icon">C</div>
        </nav>
      </header>

      <main className="main">
        <div className="logo-container">
          <h1 className="logo-text">Google</h1>
        </div>

        <form className="search-form" onSubmit={handleSearch}>
          <SearchBar 
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
          
          <div className="button-container">
            <Button type="submit" className="search-button" rounded={true}>
              Búsqueda de Google
            </Button>
          <Button type="submit" className="lucky-button" onClick={handleLucky} rounded={true}>
            Me siento con suerte
          </Button>
          </div>
        </form>

        <div className="footer">
          <p>Ofrecido por Google en: <a href="#">Español (Latinoamérica)</a></p>
        </div>
      </main>

      <footer className="footer-bar">
        <div className="footer-links">
          <a href="https://about.google/" target="_blank">Sobre Google</a>
          <a href="https://ads.google.com/" target="_blank">Publicidad</a>
          <a href="https://www.google.com/services/" target="_blank">Negocios</a>
          <a href="https://www.google.com/search/howsearchworks/" target="_blank">Cómo funciona la Búsqueda</a>
        </div>
        <div className="footer-links">
          <a href="https://policies.google.com/privacy" target="_blank">Privacidad</a>
          <a href="https://policies.google.com/terms" target="_blank">Condiciones</a>
          <a href="https://www.google.com/preferences" target="_blank">Preferencias</a>
        </div>
      </footer>
    </div>
  )
}

export default App
