import './Button.css'

function Button({ children, className, onClick, type = 'button' }) {
  return (
    <button
      type={type}
      className={`google-button ${className}`}
      onClick={onClick}
    >
      {children}
    </button>
  )
}

export default Button
