# 🎤 Rap Battle Arena Multi-Agent

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Status](https://img.shields.io/badge/status-en%20desarrollo-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

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
git clone https://github.com/tuusuario/Rap_Battle_Arena_Multi-Agent.git
cd Rap_Battle_Arena_Multi-Agent

# Instalar dependencias con uv (recomendado)
uv sync

# O con pip tradicional
pip install -r requirements.txt
```

### Uso Básico
```bash
# Ejecutar batalla con configuración por defecto
python main.py
```

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
Rap_Battle_Arena_Multi-Agent/
│
├── 📄 main.py                 # 🚀 Punto de entrada principal
├── 📄 pyproject.toml          # ⚙️ Configuración del proyecto
├── 📄 README.md               # 📚 Esta documentación
├── 📄 uv.lock                 # 🔒 Lock de dependencias
│
├── 📁 agents/                 # 🤖 Agentes del sistema
│   ├── host_agent.py          # 🎭 Maestro de ceremonias
│   ├── rapper_agent.py        # 🎤 Raperos virtuales
│   ├── judge_agent.py         # ⚖️ Juez automático
│   ├── rhyme_metric_agent.py  # 🎵 Análisis técnico
│   ├── sentiment_attack_agent.py # 😤 Análisis de agresividad
│   └── moderation_agent.py    # 🛡️ Control de contenido
│
├── 📁 api/                    # 🌐 Clientes de API
│   └── llm_client.py          # 🧠 Cliente LLM
│
├── 📁 core/                   # 🔧 Lógica central
│   ├── battle_engine.py       # ⚙️ Motor de batalla
│   └── models.py              # 📊 Modelos de datos
│
└── 📁 personas/               # 🎭 Personalidades
    └── personas.py            # 👥 Definiciones de raperos
```

## 🛠️ Desarrollo y Roadmap

### ✅ Fase 1: Diseño y Arquitectura (Completada)
- [x] Definición de agentes y responsabilidades
- [x] Modelos de datos bien estructurados
- [x] Flujo completo de batalla
- [x] Documentación técnica detallada

### 🔄 Fase 2: Motor Básico (En Progreso)
- [x] Implementación de todos los agentes
- [x] Motor de batalla funcional
- [x] Sistema de puntuación ponderada
- [ ] Suite completa de tests unitarios

### 🚧 Fase 3: Integración Inteligente (Próximo)
- [ ] Integración con AWS Bedrock
- [ ] Generación de versos con LLM
- [ ] Análisis semántico avanzado
- [ ] Personalidades más sofisticadas

### 📋 Fase 4: Experiencia Completa (Futuro)
- [ ] Interface web interactiva
- [ ] Sistema de torneos
- [ ] Métricas avanzadas y analytics
- [ ] API REST para integración externa

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor:

1. **Fork** el proyecto
2. **Crea** una rama para tu feature (`git checkout -b feature/NuevaPersonalidad`)
3. **Commit** tus cambios (`git commit -m 'Add: Nueva personalidad gangsta'`)
4. **Push** a la rama (`git push origin feature/NuevaPersonalidad`)
5. **Abre** un Pull Request

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT** - ver el archivo [LICENSE](LICENSE) para detalles.

## 👥 Autores y Reconocimientos

### Autores
- **Tu Nombre** - *Desarrollo inicial* - [@tuusuario](https://github.com/tuusuario)

### Inspiración y Reconocimientos
- 🎤 **God Level** - Por las batallas de rap épicas que inspiraron este proyecto
- 🤖 **Comunidad Multi-Agente** - Por los patrones de arquitectura distribuida
- 🎵 **Cultura Hip-Hop** - Por mantener viva la esencia de la batalla de rimas

---

<div align="center">

**🎤 ¡Que comience la batalla de rimas más épica! 🎤**

[![Reportar Bug](https://img.shields.io/badge/🐛-Reportar%20Bug-red)](https://github.com/tuusuario/Rap_Battle_Arena_Multi-Agent/issues)
[![Solicitar Feature](https://img.shields.io/badge/✨-Solicitar%20Feature-blue)](https://github.com/tuusuario/Rap_Battle_Arena_Multi-Agent/issues)
[![Documentación](https://img.shields.io/badge/📚-Documentación-green)](https://github.com/tuusuario/Rap_Battle_Arena_Multi-Agent/wiki)

*"En el ring de las palabras, solo los mejores algoritmos sobreviven"*

</div>