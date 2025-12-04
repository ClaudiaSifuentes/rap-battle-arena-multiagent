# 🎤 Rap Battle Arena Frontend

Frontend interactivo para el sistema de batallas de rap, construido con Vite + React.

## 🚀 Inicio Rápido

### Instalación

```bash
cd frontend
npm install
```

### Desarrollo

```bash
npm run dev
```

La aplicación estará disponible en `http://localhost:3000`

### Build para Producción

```bash
npm run build
```

Los archivos estáticos se generarán en la carpeta `dist/`

### Preview del Build

```bash
npm run preview
```

## 📋 Requisitos

- Node.js 18+ 
- npm o yarn
- Backend API corriendo en `http://localhost:8000` (o configurar `VITE_API_URL`)

## ⚙️ Configuración

### Variables de Entorno

Crea un archivo `.env` en la carpeta `frontend/`:

```env
VITE_API_URL=http://localhost:8000
```

Si no se especifica, por defecto usará `http://localhost:8000`.

## 🎨 Características

- ✨ **UI Moderna**: Diseño con gradientes, glassmorphism y animaciones
- 📱 **Responsive**: Funciona perfectamente en móviles y tablets
- 🎯 **Interactivo**: Formulario intuitivo para crear batallas
- 📊 **Resultados Detallados**: Visualización clara de cada ronda y ganador
- 🎭 **Selección de Personalidades**: Preview de cada rapero antes de la batalla
- ⚡ **Rápido**: Construido con Vite para desarrollo ultrarrápido

## 📁 Estructura del Proyecto

```
frontend/
├── src/
│   ├── components/
│   │   ├── BattleForm.jsx      # Formulario para crear batallas
│   │   ├── BattleResults.jsx    # Visualización de resultados
│   │   └── Header.jsx           # Encabezado de la aplicación
│   ├── services/
│   │   └── api.js               # Cliente API para comunicación con backend
│   ├── App.jsx                  # Componente principal
│   ├── App.css                  # Estilos del App
│   ├── main.jsx                 # Punto de entrada
│   └── index.css                # Estilos globales
├── index.html                   # HTML principal
├── vite.config.js              # Configuración de Vite
└── package.json                # Dependencias del proyecto
```

## 🔌 Integración con Backend

El frontend se comunica con el backend FastAPI a través de:

- `GET /personas` - Obtener personalidades disponibles
- `POST /battle` - Iniciar una nueva batalla
- `GET /health` - Health check

## 🎨 Personalización

Los colores y estilos se pueden personalizar en `src/index.css` modificando las variables CSS:

```css
:root {
  --primary: #ff6b6b;
  --secondary: #4ecdc4;
  --dark: #1a1a2e;
  --accent: #feca57;
  /* ... */
}
```

## 🐛 Troubleshooting

### Error de CORS

Si encuentras errores de CORS, asegúrate de que el backend tenga CORS habilitado para `http://localhost:3000`.

### No se conecta al backend

1. Verifica que el backend esté corriendo en `http://localhost:8000`
2. Revisa la consola del navegador para ver errores de red
3. Verifica la variable `VITE_API_URL` si está configurada

### Errores de módulos

Si encuentras errores de módulos no encontrados:

```bash
rm -rf node_modules package-lock.json
npm install
```

