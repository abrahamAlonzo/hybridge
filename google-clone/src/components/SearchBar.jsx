import { useState } from 'react'
import './SearchBar.css'

function SearchBar({ value, onChange }) {
  const [isFocused, setIsFocused] = useState(false)

  return (
    <div className={`search-bar-wrapper ${isFocused ? 'focused' : ''}`}>
      <div className="search-icon">
        <svg focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
          <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"></path>
        </svg>
      </div>
      
      <input
        type="text"
        className="search-input"
        value={value}
        onChange={onChange}
        onFocus={() => setIsFocused(true)}
        onBlur={() => setIsFocused(false)}
        placeholder="Buscar en Google o escribir una URL"
      />
      
      <div className="search-actions">
        {value && (
          <button
            type="button"
            className="clear-button"
            onClick={() => onChange({ target: { value: '' } })}
          >
            <svg viewBox="0 0 24 24">
              <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
            </svg>
          </button>
        )}
        <div className="divider"></div>
        <button type="button" className="voice-button">
          <svg viewBox="0 0 24 24">
            <path d="M12 3c-1.66 0-3 1.34-3 3v6c0 1.66 1.34 3 3 3s3-1.34 3-3V6c0-1.66-1.34-3-3-3zm3.89 5.89c-.42-.14-.87-.21-1.37-.27v5.76c0 .55-.45 1-1 1s-1-.45-1-1V8.62c-.5.06-.95.13-1.37.27C9.85 9.02 8.5 11.13 8.5 13.5c0 2.48 2.02 4.5 4.5 4.5s4.5-2.02 4.5-4.5c0-2.37-1.35-4.48-3.51-5.61zm-.38 5.61H12c-.55 0-1-.45-1-1s.45-1 1-1h3.5c.55 0 1 .45 1 1s-.45 1-1 1z"></path>
          </svg>
        </button>
        <button type="button" className="lens-button">
          <svg viewBox="0 0 24 24">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"></path>
          </svg>
        </button>
      </div>
    </div>
  )
}

export default SearchBar
