#!/bin/bash
# scripts/setup.sh
# Script para configurar el proyecto completo

echo "🔧 Configurando Rap Battle Arena Multi-Agent"
echo "============================================"

# Verificar si estamos en el directorio correcto
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: Ejecuta este script desde el directorio raíz del proyecto"
    exit 1
fi

echo "1. 🐍 Configurando entorno Python..."

# Crear entorno virtual si no existe
if [ ! -d ".venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv .venv
fi

# Activar entorno virtual
echo "📦 Activando entorno virtual..."
source .venv/bin/activate

# Instalar dependencias Python
echo "📥 Instalando dependencias Python..."
if command -v uv &> /dev/null; then
    echo "🚀 Usando uv (más rápido)..."
    uv sync
else
    echo "📦 Usando pip..."
    pip install -r requirements.txt 2>/dev/null || {
        echo "📋 Creando requirements.txt..."
        cat > requirements.txt << EOF
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
python-multipart==0.0.6
EOF
        pip install -r requirements.txt
    }
fi

echo "2. 🌐 Configurando frontend..."

# Ir al directorio del frontend
cd frontend

# Verificar Node.js
if ! command -v node &> /dev/null; then
    echo "⚠️ Advertencia: Node.js no está instalado"
    echo "📥 Descarga desde: https://nodejs.org/"
else
    echo "📦 Instalando dependencias del frontend..."
    npm install
fi

cd ..

echo "3. 📋 Creando archivo de configuración de ejemplo..."

# Crear .env.example si no existe
if [ ! -f ".env.example" ]; then
    cat > .env.example << EOF
# Configuración de API Keys - NO PONER VALORES REALES AQUÍ
# Copiar este archivo a .env y completar con valores reales

# OpenAI API
OPENAI_API_KEY=tu_openai_api_key_aqui

# AWS Bedrock
AWS_ACCESS_KEY_ID=tu_aws_access_key_aqui
AWS_SECRET_ACCESS_KEY=tu_aws_secret_key_aqui
AWS_REGION=us-east-1

# Configuración de la aplicación
BATTLE_ROUNDS=3
JUDGE_STRICT_MODE=true
MODERATION_LEVEL=medium
EOF
fi

echo ""
echo "✅ ¡Configuración completada!"
echo ""
echo "📋 Próximos pasos:"
echo "1. Copia .env.example a .env y configura tus API keys"
echo "2. Ejecuta el backend: ./scripts/run_backend.sh"
echo "3. En otra terminal, ejecuta el frontend: ./scripts/run_frontend.sh"
echo ""
echo "🌐 URLs importantes:"
echo "   Frontend: http://localhost:5173"
echo "   API: http://localhost:8000"
echo "   Documentación API: http://localhost:8000/docs"
