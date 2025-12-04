# 🚀 Rap Battle Arena API

API REST construida con FastAPI para servir el sistema de batallas de rap multi-agente.

## 📋 Endpoints Disponibles

### `GET /`
Health check básico.

**Respuesta:**
```json
{
  "status": "ok",
  "message": "Rap Battle Arena API está funcionando"
}
```

### `GET /health`
Health check detallado.

**Respuesta:**
```json
{
  "status": "ok",
  "message": "API está funcionando correctamente"
}
```

### `GET /personas`
Obtiene todas las personalidades de raperos disponibles.

**Respuesta:**
```json
{
  "personas": [
    {
      "id": "fast_technical",
      "name": "Rápido Técnico",
      "language": "es",
      "flow_speed": "fast",
      "aggressiveness": "high",
      "complexity": "high",
      "style_description": "..."
    },
    ...
  ]
}
```

### `GET /personas/{persona_id}`
Obtiene información de una personalidad específica.

**Parámetros:**
- `persona_id` (path): ID de la personalidad

**Respuesta:**
```json
{
  "id": "fast_technical",
  "name": "Rápido Técnico",
  "language": "es",
  "flow_speed": "fast",
  "aggressiveness": "high",
  "complexity": "high",
  "style_description": "..."
}
```

### `POST /battle`
Inicia una nueva batalla de rap.

**Body (JSON):**
```json
{
  "topic": "Quién domina más el escenario",
  "persona_A": "fast_technical",
  "persona_B": "punchline_master",
  "rounds": 3
}
```

**Parámetros:**
- `topic` (requerido): Tema de la batalla
- `persona_A` (opcional, default: "fast_technical"): ID de la personalidad del rapero A
- `persona_B` (opcional, default: "punchline_master"): ID de la personalidad del rapero B
- `rounds` (opcional, default: 3, rango: 1-10): Número de rondas

**Respuesta:**
```json
{
  "topic": "Quién domina más el escenario",
  "rounds": [
    {
      "round_number": 1,
      "score_A": 0.785,
      "score_B": 0.623,
      "winner": "A",
      "verse_A": {
        "rapper_id": "A",
        "round_number": 1,
        "persona_id": "fast_technical",
        "text": "Llegué al escenario como un huracán..."
      },
      "verse_B": {
        "rapper_id": "B",
        "round_number": 1,
        "persona_id": "punchline_master",
        "text": "Hablas de fuego pero yo soy el volcán..."
      }
    },
    ...
  ],
  "overall_winner": "A"
}
```

## 🚀 Ejecutar la API

### Opción 1: Usando el script principal
```bash
python api_main.py
```

### Opción 2: Usando uvicorn directamente
```bash
uvicorn api.battle_api:app --host 0.0.0.0 --port 8000 --reload
```

### Opción 3: Usando uv
```bash
uv run python api_main.py
```

La API estará disponible en: `http://localhost:8000`

## 📚 Documentación Interactiva

Una vez que la API esté corriendo, puedes acceder a:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🔧 Ejemplo de Uso con cURL

### Iniciar una batalla
```bash
curl -X POST "http://localhost:8000/battle" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Quién domina más el escenario",
    "persona_A": "fast_technical",
    "persona_B": "punchline_master",
    "rounds": 3
  }'
```

### Obtener personalidades disponibles
```bash
curl "http://localhost:8000/personas"
```

### Health check
```bash
curl "http://localhost:8000/health"
```

## 🔧 Ejemplo de Uso con Python

```python
import requests

# Iniciar una batalla
response = requests.post(
    "http://localhost:8000/battle",
    json={
        "topic": "Quién domina más el escenario",
        "persona_A": "fast_technical",
        "persona_B": "punchline_master",
        "rounds": 3
    }
)

result = response.json()
print(f"Ganador: {result['overall_winner']}")
for round_data in result['rounds']:
    print(f"Ronda {round_data['round_number']}: {round_data['winner']}")
```

## ⚙️ Configuración

Asegúrate de tener configuradas las credenciales de AWS para que la API pueda usar Bedrock:

```bash
# Windows PowerShell
$env:AWS_ACCESS_KEY_ID="your-access-key"
$env:AWS_SECRET_ACCESS_KEY="your-secret-key"
$env:AWS_REGION="us-east-1"
```

O configura AWS CLI:
```bash
aws configure
```

## 🌐 CORS

La API está configurada con CORS habilitado para todos los orígenes (`*`). En producción, deberías especificar los dominios permitidos en `api/battle_api.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Especificar dominios
    ...
)
```

