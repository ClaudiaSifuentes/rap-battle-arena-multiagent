# 🎤 Rap Battle Arena Multi-Agent

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![React](https://img.shields.io/badge/React-18-blue.svg)
![Status](https://img.shields.io/badge/status-MVP%20Completo-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange.svg)

Un sistema multi-agente inteligente que simula batallas de rap 1 vs 1, donde raperos virtuales con diferentes personalidades generan versos y agentes especializados analizan técnicamente cada performance para determinar automáticamente al ganador.

## 🎯 Descripción del Proyecto

### Problema
Las batallas de rap tipo torneo (estilo God Level) son evaluadas de forma subjetiva por jueces humanos, lo que puede generar sesgos y poca transparencia. Además, no se aprovechan herramientas de IA para analizar técnicamente las rimas, la métrica y la agresividad lírica de los participantes.

### Objetivo
Diseñar e implementar un sistema multi-agente que simule batallas de rap 1 vs 1, donde raperos virtuales con diferentes personalidades generen versos y un conjunto de agentes especializados analicen técnicamente cada verso para determinar automáticamente al ganador de cada ronda y de la batalla completa.

## ✨ Características Principales

- 🎭 **Sistema Multi-Agente**: Arquitectura modular con agentes especializados
- 🎤 **Raperos Virtuales**: Diferentes personalidades y estilos de rap
- 📊 **Análisis Técnico**: Evaluación automática de rima, métrica y agresividad
- ⚖️ **Juicio Automático**: Sistema de puntuación objetivo y transparente
- 🛡️ **Moderación de Contenido**: Filtros automáticos para contenido apropiado
- 🔄 **Batallas Completas**: Sistema de rondas con ganador global
- 🌐 **API REST**: Interfaz completa para integración externa
- 🎨 **Interfaz Web**: Frontend moderno con React y Vite
- 🚀 **Despliegue Fácil**: Scripts automatizados para desarrollo y producción
- ⚙️ **Configuración Flexible**: Sistema de configuración centralizado


## 🤖 Arquitectura del Sistema

### Agentes del Sistema

#### 🎭 **HostAgent** - Maestro de Ceremonias

- **Responsabilidad**: Coordinar toda la batalla y gestionar el flujo de eventos
- **Input**: Configuración (tema, número de rondas, personalidades)
- **Output**: BattleResult completo con todos los resultados

#### 🎤 **RapperAgent** - Raperos Virtuales (A y B)
- **Responsabilidad**: Generar versos según personalidad y contexto
- **Input**: Personalidad, tema, verso del oponente (opcional)
- **Output**: Verse con texto y metadata

#### 🎵 **RhymeMetricAgent** - Análisis Técnico
- **Responsabilidad**: Evaluar calidad de rima y métrica
- **Output**: `rhyme_score`, `metric_score`, detalles técnicos

#### 😤 **SentimentAttackAgent** - Análisis de Agresividad
- **Responsabilidad**: Medir intensidad competitiva y tono
- **Output**: `sentiment_score`, `attack_score`

#### 🛡️ **ModerationAgent** - Control de Contenido
- **Responsabilidad**: Verificar cumplimiento de reglas
- **Output**: `penalty_score`, `is_allowed`

#### ⚖️ **JudgeAgent** - Juez Automático
- **Responsabilidad**: Combinar métricas y decidir ganadores
- **Output**: `RoundResult` con puntuaciones y ganador

## 📊 Modelos de Datos

```python
@dataclass
class Verse:
    rapper_id: str       
    round_number: int
    persona_id: str
    text: str

@dataclass
class AnalysisResult:
    rhyme_score: float
    metric_score: float
    attack_score: float
    sentiment_score: float
    penalty_score: float
    
    def total_score(self, weights: Optional[Dict[str, float]] = None) -> float:
        """Calcula puntuación total ponderada"""

@dataclass
class RoundResult:
    round_number: int
    score_A: float
    score_B: float
    winner: str          
    verse_A: Verse
    verse_B: Verse

@dataclass
class BattleResult:
    topic: str
    rounds: List[RoundResult]
    overall_winner: str   
```

## 🔄 Flujo de Batalla

### Proceso Detallado

HostAgent inicia batalla con:

Tema (ej. “Quién domina más el escenario”).

Nº de rondas (ej. 3).

Personalidades de A y B.

Para cada ronda i:

Host pide a RapperAgent A que genere su verso → Verse A.

Host pide a RapperAgent B que responda al verso de A → Verse B.

Host envía Verse A y Verse B a:

RhymeMetricAgent

SentimentAttackAgent

ModerationAgent

Cada agente devuelve sus métricas para A y B.

Host envía todos los análisis a JudgeAgent.

JudgeAgent devuelve RoundResult (score A/B + ganador).

(Opcional) Host pide CrowdAgent una reacción basada en RoundResult.

Host guarda RoundResult en la lista de la batalla.

Al final de todas las rondas:

Host suma resultados y determina overall_winner.

Construye BattleResult.


sequenceDiagram
    participant Host as HostAgent
    participant RA as RapperAgent A
    participant RB as RapperAgent B
    participant RM as RhymeMetricAgent
    participant SA as SentimentAttackAgent
    participant MA as ModerationAgent
    participant J as JudgeAgent

    Host->>Host: Iniciar batalla (tema, rondas, personalidades)

    loop Por cada ronda
        Host->>RA: generate_verse(persona_A, topic, last_verse_B)
        RA-->>Host: Verse A

        Host->>RB: generate_verse(persona_B, topic, last_verse_A)
        RB-->>Host: Verse B

        par Análisis verso A
            Host->>RM: analyze(Verse A)
            RM-->>Host: metrics_A
            Host->>SA: analyze(Verse A)
            SA-->>Host: attack_A
            Host->>MA: moderate(Verse A)
            MA-->>Host: penalty_A
        and Análisis verso B
            Host->>RM: analyze(Verse B)
            RM-->>Host: metrics_B
            Host->>SA: analyze(Verse B)
            SA-->>Host: attack_B
            Host->>MA: moderate(Verse B)
            MA-->>Host: penalty_B
        end

        Host->>J: judge_round(data_A, data_B)
        J-->>Host: RoundResult
        Host->>Host: Guardar RoundResult
    end

    Host->>Host: Calcular BattleResult (ganador global)





---

## 🚀 Instalación y Uso

### Prerrequisitos
```bash
Python 3.8+
uv (recomendado) o pip
```

### Instalación Rápida
```bash
# Clonar repositorio
git clone https://github.com/ClaudiaSifuentes/rap-battle-arena-multiagent.git
cd rap-battle-arena-multiagent

# Configuración automática del proyecto
./scripts/setup.sh
```

### Uso Básico

#### Opción 1: Línea de Comandos (Básico)
```bash
# Ejecutar batalla con configuración por defecto
python main.py
```

#### Opción 2: Aplicación Web Completa (Recomendado)
```bash
# Terminal 1: Backend API
./scripts/run_backend.sh

# Terminal 2: Frontend Web
./scripts/run_frontend.sh
```

Luego abrir en el navegador: `http://localhost:5173`

### Ejemplo de Salida
```
TEMA: Quién domina más el escenario
============================================================

Ronda 1 → Ganador: A
  Score A: 0.785
  Score B: 0.623
------------------------------------------------------------
[Rapero A]
Llegué al escenario como un huracán,
mis barras son fuego que te van a quemar...

[Rapero B]  
Hablas de fuego pero yo soy el volcán,
tus rimas son débiles, no me van a parar...
------------------------------------------------------------

GANADOR GLOBAL: A
```

## 📁 Estructura del Proyecto

```
rap-battle-arena-multiagent/
│
├── 📄 main.py                 # 🚀 Punto de entrada básico
├── 📄 api_main.py             # 🌐 Servidor API
├── 📄 pyproject.toml          # ⚙️ Configuración del proyecto
├── 📄 README.md               # 📚 Esta documentación
├── 📄 .env.example            # � Plantilla de configuración
│
├── 📁 agents/                 # 🤖 Agentes del sistema
│   ├── host_agent.py          # 🎭 Maestro de ceremonias
│   ├── rapper_agent.py        # 🎤 Raperos virtuales
│   ├── judge_agent.py         # ⚖️ Juez automático
│   ├── rhyme_metric_agent.py  # 🎵 Análisis técnico
│   ├── sentiment_attack_agent.py # 😤 Análisis de agresividad
│   └── moderation_agent.py    # 🛡️ Control de contenido
│
├── 📁 api/                    # 🌐 API REST
│   ├── battle_api.py          # 🚀 Endpoints principales
│   ├── schemas.py             # 📋 Esquemas de datos
│   └── llm_client.py          # 🧠 Cliente LLM
│
├── 📁 core/                   # 🔧 Lógica central
│   ├── battle_engine.py       # ⚙️ Motor de batalla
│   └── models.py              # 📊 Modelos de datos
│
├── 📁 personas/               # 🎭 Personalidades de raperos
│   └── personas.py            # 👥 Definiciones y estilos
│
├── 📁 frontend/               # 🎨 Interfaz web (React)
│   ├── src/                   # 📱 Código fuente
│   ├── package.json           # 📦 Dependencias Node.js
│   └── vite.config.js         # ⚡ Configuración de Vite
│
├── 📁 config/                 # ⚙️ Configuración
│   └── settings.py            # 🔧 Configuración centralizada
│
├── 📁 scripts/                # 🛠️ Scripts de automatización
│   ├── setup.sh               # 🔧 Configuración inicial
│   ├── run_backend.sh         # 🚀 Ejecutar backend
│   └── run_frontend.sh        # 🎨 Ejecutar frontend
│
├── 📁 docs/                   # 📚 Documentación
│   ├── API_README.md          # 📖 Documentación API
│   ├── FRONTEND_SETUP.md      # 🎨 Configuración frontend
│   └── AWS_SETUP.md           # ☁️ Configuración AWS
│
└── 📁 tests/                  # 🧪 Tests automatizados
    ├── test_api.py            # 🌐 Tests de API
    └── conftest.py            # ⚙️ Configuración de tests
```

## 🛠️ Desarrollo y Roadmap

### ✅ Fase 1: Diseño y Arquitectura (Completada)
- [x] Definición de agentes y responsabilidades
- [x] Modelos de datos bien estructurados
- [x] Flujo completo de batalla
- [x] Documentación técnica detallada

### ✅ Fase 2: Motor Básico (Completada)
- [x] Implementación de todos los agentes
- [x] Motor de batalla funcional
- [x] Sistema de puntuación ponderada
- [x] API REST completa con FastAPI
- [x] Interfaz web con React/Vite
- [x] Scripts de automatización
- [x] Estructura de proyecto organizada
- [ ] Suite completa de tests unitarios

### 🚧 Fase 3: Integración Inteligente (En Progreso)
- [x] Base para integración con LLMs
- [ ] Integración con AWS Bedrock
- [ ] Integración con OpenAI GPT
- [ ] Generación inteligente de versos
- [ ] Análisis semántico avanzado
- [ ] Personalidades más sofisticadas
- [ ] Sistema de aprendizaje adaptativo

### 📋 Fase 4: Experiencia Completa (Futuro)
- [ ] Sistema de torneos multi-eliminación
- [ ] Métricas avanzadas y analytics
- [ ] Base de datos para historial de batallas
- [ ] Sistema de usuarios y perfiles
- [ ] Streaming en vivo de batallas
- [ ] Integración con redes sociales
- [ ] Modo multijugador

## 📊 Tecnologías Utilizadas

### Backend
- **Python 3.8+** - Lenguaje principal
- **FastAPI** - Framework web moderno y rápido
- **Uvicorn** - Servidor ASGI de alto rendimiento
- **Pydantic** - Validación de datos con tipos

### Frontend
- **React 18** - Biblioteca de interfaz de usuario
- **Vite** - Herramienta de construcción rápida
- **JavaScript ES6+** - Lenguaje del frontend
- **CSS3** - Estilos y animaciones

### Herramientas de Desarrollo
- **uv** - Gestor de dependencias Python ultra-rápido
- **npm** - Gestor de paquetes Node.js
- **Git** - Control de versiones
- **Make** - Automatización de tareas
- **Bash Scripts** - Scripts de automatización

### Arquitectura
- **Multi-Agent System** - Patrón de agentes especializados
- **REST API** - Comunicación cliente-servidor
- **Separation of Concerns** - Separación clara de responsabilidades
- **Configuration Management** - Gestión centralizada de configuración

## 📈 Estadísticas del Proyecto

```
Líneas de Código:    ~2,500
Archivos Python:     ~15
Componentes React:   ~8
Agentes IA:          6
Personalidades:      3+
API Endpoints:       5+
```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor:

1. **Fork** el proyecto
2. **Crea** una rama para tu feature (`git checkout -b feature/NuevaPersonalidad`)
3. **Commit** tus cambios (`git commit -m 'Add: Nueva personalidad gangsta'`)
4. **Push** a la rama (`git push origin feature/NuevaPersonalidad`)
5. **Abre** un Pull Request

### Tipos de Contribuciones

- 🎤 **Nuevas Personalidades**: Añadir estilos únicos de rap
- 🧠 **Algoritmos de IA**: Mejorar análisis técnico
- 🎨 **Mejoras de UI/UX**: Hacer la interfaz más atractiva
- 🧪 **Tests**: Añadir cobertura de testing
- 📚 **Documentación**: Mejorar guías y ejemplos
- 🐛 **Bug Fixes**: Corregir errores encontrados
- ⚡ **Optimizaciones**: Mejorar rendimiento

### Guidelines de Desarrollo

- Seguir las convenciones de código existentes
- Añadir tests para nuevas funcionalidades
- Actualizar documentación según sea necesario
- Usar mensajes de commit descriptivos en español
- Mantener las funciones pequeñas y enfocadas

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT** - ver el archivo [LICENSE](LICENSE) para detalles.

## 👥 Autores y Reconocimientos

### Autores
- **Claudia Sifuentes** - [@ClaudiaSifuentes](https://github.com/ClaudiaSifuentes)
- **Marcelo Poggi** - [@Singoe123](https://github.com/Singoe123)
- **Sebastian Valdivia** - [@sebasvp2005](https://github.com/sebasvp2005)
- **Daniella Vargas** - [@lucumango](https://github.com/lucumango)

### Inspiración y Reconocimientos
- 🎤 **God Level** - Por las batallas de rap épicas que inspiraron este proyecto
- 🤖 **Comunidad Multi-Agente** - Por los patrones de arquitectura distribuida
- 🎵 **Cultura Hip-Hop** - Por mantener viva la esencia de la batalla de rimas

---

<div align="center">

**🎤 ¡Que comience la batalla de rimas más épica! 🎤**

[![Reportar Bug](https://img.shields.io/badge/🐛-Reportar%20Bug-red)](https://github.com/ClaudiaSifuentes/rap-battle-arena-multiagent/issues)
[![Solicitar Feature](https://img.shields.io/badge/✨-Solicitar%20Feature-blue)](https://github.com/ClaudiaSifuentes/rap-battle-arena-multiagent/issues)
[![Documentación](https://img.shields.io/badge/📚-Documentación-green)](https://github.com/ClaudiaSifuentes/rap-battle-arena-multiagent/wiki)

*"En el ring de las palabras, solo los mejores algoritmos sobreviven"*

</div>

## 🛠️ Comandos Make (Opcional)

Si prefieres usar Make para gestionar el proyecto:

```bash
make help          # Ver todos los comandos disponibles
make setup         # Configuración inicial completa
make backend       # Ejecutar solo backend
make frontend      # Ejecutar solo frontend
make basic         # Ejecutar versión de consola
make clean         # Limpiar archivos temporales
make status        # Ver estado del proyecto
make urls          # Ver URLs importantes
```

## ⚙️ Configuración Avanzada

### Variables de Entorno

Crea un archivo `.env` basado en `.env.example`:

```bash
# Copiar plantilla de configuración
cp .env.example .env
```

Configurar las variables según tus necesidades:

```env
# API Keys (opcionales para desarrollo básico)
OPENAI_API_KEY=tu_clave_openai_aqui
AWS_ACCESS_KEY_ID=tu_aws_access_key
AWS_SECRET_ACCESS_KEY=tu_aws_secret_key
AWS_REGION=us-east-1

# Configuración de batalla
BATTLE_ROUNDS=3
JUDGE_STRICT_MODE=true
MODERATION_LEVEL=medium

# Configuración del servidor
HOST=0.0.0.0
PORT=8000
DEBUG=true
```

### Personalización de Agentes

Puedes modificar las personalidades de los raperos en `personas/personas.py`:

```python
RAPPER_PERSONAS = {
    "tu_nueva_personalidad": {
        "style": "Tu estilo único",
        "strengths": ["característica 1", "característica 2"],
        "weaknesses": ["debilidad 1"],
        "vocabulary": "tipo de vocabulario",
        "flow_pattern": "patrón de flow"
    }
}
```

### Configuración de Puntuación

Ajusta los pesos de evaluación en `config/settings.py`:

```python
DEFAULT_SCORING_WEIGHTS = {
    'rhyme': 0.30,      # Peso de la rima
    'metric': 0.25,     # Peso de la métrica
    'attack': 0.25,     # Peso del ataque
    'sentiment': 0.15,  # Peso del sentimiento
    'penalty': -0.05    # Penalización
}
```

## 🔧 Troubleshooting

### Problemas Comunes

#### ❌ **Error: "Failed to fetch"**
```bash
# Solución: Verificar que ambos servidores estén corriendo
./scripts/run_backend.sh    # Terminal 1
./scripts/run_frontend.sh   # Terminal 2
```

#### ❌ **Error: "Port 8000 already in use"**
```bash
# Solución: Cambiar puerto o matar proceso
export PORT=8080  # Cambiar puerto
# O matar proceso existente
lsof -ti:8000 | xargs kill -9
```

#### ❌ **Error: "Node.js not found"**
```bash
# Solución: Instalar Node.js
# Ubuntu/Debian:
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# O usar nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 18
```

#### ❌ **Error: Permission denied en scripts**
```bash
# Solución: Hacer scripts ejecutables
chmod +x scripts/*.sh
```

### FAQ (Preguntas Frecuentes)

**Q: ¿Puedo usar el proyecto sin API keys?**
A: Sí, el sistema funciona con versos pre-generados. Las API keys solo son necesarias para generación automática con LLMs.

**Q: ¿Cómo añado nuevas personalidades de raperos?**
A: Edita el archivo `personas/personas.py` y añade tu nueva personalidad siguiendo el formato existente.

**Q: ¿El proyecto funciona en Windows?**
A: Sí, pero recomendamos usar Git Bash o WSL para ejecutar los scripts bash.

**Q: ¿Puedo cambiar los criterios de puntuación?**
A: Sí, modifica los pesos en `config/settings.py` o usa variables de entorno.

**Q: ¿Cómo contribuyo al proyecto?**
A: Haz un fork, crea una rama, desarrolla tu feature y envía un pull request.

## 🚀 Despliegue en Producción

### Docker (Recomendado)

```bash
# TODO: Implementar Dockerfile
# docker build -t rap-battle-arena .
# docker run -p 8000:8000 rap-battle-arena
```

### Manual

```bash
# Configurar para producción
export DEBUG=false
export HOST=0.0.0.0
export PORT=80

# Construir frontend
cd frontend && npm run build

# Servir con nginx o similar
# TODO: Añadir configuración de nginx
```