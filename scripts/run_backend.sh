#!/bin/bash
# scripts/run_backend.sh
# Script para ejecutar el backend del proyecto

echo "🚀 Iniciando Rap Battle Arena - Backend API"
echo "==========================================="

# Verificar si estamos en el directorio correcto
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: Ejecuta este script desde el directorio raíz del proyecto"
    exit 1
fi

# Activar entorno virtual si existe
if [ -d ".venv" ]; then
    echo "📦 Activando entorno virtual..."
    source .venv/bin/activate
else
    echo "⚠️ Advertencia: No se encontró entorno virtual (.venv)"
fi

# Verificar dependencias
echo "🔍 Verificando dependencias..."
if ! python -c "import uvicorn, fastapi" 2>/dev/null; then
    echo "📥 Instalando dependencias..."
    if command -v uv &> /dev/null; then
        uv sync
    else
        pip install -r requirements.txt 2>/dev/null || pip install uvicorn fastapi
    fi
fi

# Ejecutar el servidor
echo "🎤 Iniciando servidor API en http://localhost:8000"
echo "📚 Documentación disponible en http://localhost:8000/docs"
echo "⏹️ Presiona Ctrl+C para detener"
echo ""

python api_main.py
