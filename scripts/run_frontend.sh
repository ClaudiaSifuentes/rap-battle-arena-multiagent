#!/bin/bash
# scripts/run_frontend.sh
# Script para ejecutar el frontend del proyecto

echo "🎨 Iniciando Rap Battle Arena - Frontend"
echo "======================================="

# Verificar si estamos en el directorio correcto
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: Ejecuta este script desde el directorio raíz del proyecto"
    exit 1
fi

# Ir al directorio del frontend
cd frontend

# Verificar si existe package.json
if [ ! -f "package.json" ]; then
    echo "❌ Error: No se encontró package.json en el directorio frontend"
    exit 1
fi

# Verificar Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Error: Node.js no está instalado"
    echo "📥 Instala Node.js desde: https://nodejs.org/"
    exit 1
fi

# Verificar npm
if ! command -v npm &> /dev/null; then
    echo "❌ Error: npm no está instalado"
    exit 1
fi

echo "📦 Verificando/instalando dependencias..."
npm install

echo "🎨 Iniciando servidor de desarrollo..."
echo "🌐 Frontend disponible en http://localhost:5173"
echo "⏹️ Presiona Ctrl+C para detener"
echo ""

npm run dev
