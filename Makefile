# Makefile para Rap Battle Arena Multi-Agent
.PHONY: help setup install backend frontend clean test lint format

# Variables
VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

help: ## Mostrar esta ayuda
	@echo "Rap Battle Arena Multi-Agent - Comandos disponibles:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Configuración inicial completa del proyecto
	@echo "🔧 Configurando proyecto..."
	@chmod +x scripts/*.sh
	@./scripts/setup.sh

install: ## Instalar solo dependencias Python
	@echo "📦 Instalando dependencias Python..."
	@python3 -m venv $(VENV_DIR) || true
	@$(PIP) install --upgrade pip
	@if command -v uv >/dev/null 2>&1; then \
		uv sync; \
	else \
		$(PIP) install fastapi uvicorn python-multipart; \
	fi

frontend-install: ## Instalar dependencias del frontend
	@echo "🎨 Instalando dependencias del frontend..."
	@cd frontend && npm install

backend: ## Ejecutar solo el backend
	@echo "🚀 Iniciando backend..."
	@./scripts/run_backend.sh

frontend: ## Ejecutar solo el frontend  
	@echo "🎨 Iniciando frontend..."
	@./scripts/run_frontend.sh

dev: ## Ejecutar modo desarrollo (requiere 2 terminales)
	@echo "🚀 Para desarrollo necesitas 2 terminales:"
	@echo "  Terminal 1: make backend"
	@echo "  Terminal 2: make frontend"

basic: ## Ejecutar versión básica (solo consola)
	@echo "🎤 Ejecutando batalla básica..."
	@$(PYTHON) main.py

clean: ## Limpiar archivos temporales
	@echo "🧹 Limpiando archivos temporales..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@cd frontend && npm cache clean --force 2>/dev/null || true

test: ## Ejecutar tests (TODO: implementar)
	@echo "🧪 Tests no implementados aún..."
	@echo "TODO: Implementar pytest"

lint: ## Verificar código (TODO: implementar)
	@echo "🔍 Linting no implementado aún..."
	@echo "TODO: Implementar flake8, black, mypy"

format: ## Formatear código (TODO: implementar)
	@echo "✨ Formateo no implementado aún..."
	@echo "TODO: Implementar black, isort"

docs: ## Generar documentación
	@echo "📚 Abriendo documentación..."
	@echo "README: file://$(PWD)/README.md"
	@echo "API Docs: http://localhost:8000/docs (cuando backend esté corriendo)"

status: ## Mostrar estado del proyecto
	@echo "📊 Estado del proyecto:"
	@echo "Python: $(shell python3 --version 2>/dev/null || echo 'No instalado')"
	@echo "Node.js: $(shell node --version 2>/dev/null || echo 'No instalado')"
	@echo "npm: $(shell npm --version 2>/dev/null || echo 'No instalado')"
	@echo "uv: $(shell uv --version 2>/dev/null || echo 'No instalado')"
	@echo "Venv: $(shell test -d $(VENV_DIR) && echo 'Configurado' || echo 'No configurado')"
	@echo "Frontend deps: $(shell test -d frontend/node_modules && echo 'Instaladas' || echo 'No instaladas')"

urls: ## Mostrar URLs importantes
	@echo "🌐 URLs del proyecto:"
	@echo "  Frontend:        http://localhost:5173"
	@echo "  API Backend:     http://localhost:8000"
	@echo "  API Docs:        http://localhost:8000/docs"
	@echo "  Redoc:           http://localhost:8000/redoc"
