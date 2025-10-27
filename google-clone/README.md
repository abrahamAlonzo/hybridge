# Google Clone - Clon del Buscador de Google

Un clon del buscador de Google construido con React y Vite, con microinteracciones y diseño fiel al original.

## Características

- ✅ Diseño similar a Google.com
- ✅ Microinteracciones con efectos hover en botones
- ✅ Barra de búsqueda con iconos interactivos
- ✅ Resaltado de elementos al pasar el mouse
- ✅ Responsive design
- ✅ Animaciones suaves y transiciones

## Tecnologías Utilizadas

- React 18.3
- Vite 7.1
- CSS3 con animaciones y transiciones

## Instalación

1. Navega a la carpeta del proyecto:
```bash
cd google-clone
```

2. Instala las dependencias:
```bash
npm install
```

3. Inicia el servidor de desarrollo:
```bash
npm run dev
```

4. Abre tu navegador en la URL que se muestra en la terminal (usualmente `http://localhost:5173`)

## Scripts Disponibles

- `npm run dev` - Inicia el servidor de desarrollo
- `npm run build` - Construye la aplicación para producción
- `npm run preview` - Previsualiza la build de producción

## Estructura del Proyecto

```
google-clone/
├── public/
├── src/
│   ├── components/
│   │   ├── Button.jsx       # Componente de botón
│   │   ├── Button.css       # Estilos del botón
│   │   ├── SearchBar.jsx    # Componente de barra de búsqueda
│   │   └── SearchBar.css    # Estilos de la barra
│   ├── App.jsx              # Componente principal
│   ├── App.css              # Estilos principales
│   ├── index.css            # Estilos globales
│   └── main.jsx             # Punto de entrada
├── index.html
├── vite.config.js
└── package.json
```

## Microinteracciones Implementadas

1. **Botones de navegación**: Efecto hover con fondo gris claro
2. **Barra de búsqueda**: Sombra al hover y focus
3. **Botones de búsqueda**: Sombra y cambio de color en hover
4. **Botón de usuario**: Sombra al pasar el mouse
5. **Iconos interactivos**: Resaltado con fondo en hover
6. **Enlaces del footer**: Subrayado en hover

## Personalización

Puedes modificar los colores y estilos editando los archivos CSS en la carpeta `src/`:

- `src/App.css` - Estilos principales y layout
- `src/components/SearchBar.css` - Estilos de la barra de búsqueda
- `src/components/Button.css` - Estilos de los botones

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo.
