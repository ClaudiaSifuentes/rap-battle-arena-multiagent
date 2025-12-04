# api/battle_api.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from api.schemas import (
    BattleRequest,
    BattleResultSchema,
    RoundResultSchema,
    VerseSchema,
    PersonasResponse,
    PersonaInfo,
    HealthResponse,
)
from personas.personas import RAPPER_PERSONAS
from agents.rapper_agent import RapperAgent
from agents.rhyme_metric_agent import RhymeMetricAgent
from agents.sentiment_attack_agent import SentimentAttackAgent
from agents.moderation_agent import ModerationAgent
from agents.judge_agent import JudgeAgent
from agents.host_agent import HostAgent
from core.battle_engine import BattleEngine
from core.models import BattleResult, Verse, RoundResult


app = FastAPI(
    title="Rap Battle Arena API",
    description="API para simular batallas de rap 1 vs 1 con agentes especializados",
    version="0.1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_battle_engine(
    persona_A_id: str,
    persona_B_id: str,
    rounds: int,
    style_description_A: str | None = None,
    style_description_B: str | None = None,
    description_A: str | None = None,
    description_B: str | None = None,
) -> BattleEngine:
    """Crea un BattleEngine con los raperos y agentes configurados"""
    # Manejar rapero personalizado (solo con descripción adicional)
    if persona_A_id == "custom":
        if not description_A:
            raise HTTPException(
                status_code=400,
                detail="Para un rapero personalizado, se requiere una descripción adicional"
            )
        persona_A = {
            "name": "Rapero Personalizado",
            "language": "es",
            "flow_speed": "medium",
            "aggressiveness": "medium",
            "complexity": "medium",
            "style_description": description_A,
        }
    else:
        if persona_A_id not in RAPPER_PERSONAS:
            raise HTTPException(
                status_code=400,
                detail=f"Persona '{persona_A_id}' no encontrada"
            )
        persona_A = RAPPER_PERSONAS[persona_A_id].copy()
        # Si se envía style_description desde el frontend, usarlo en lugar del del backend
        if style_description_A:
            persona_A["style_description"] = style_description_A
    
    if persona_B_id == "custom":
        if not description_B:
            raise HTTPException(
                status_code=400,
                detail="Para un rapero personalizado, se requiere una descripción adicional"
            )
        persona_B = {
            "name": "Rapero Personalizado",
            "language": "es",
            "flow_speed": "medium",
            "aggressiveness": "medium",
            "complexity": "medium",
            "style_description": description_B,
        }
    else:
        if persona_B_id not in RAPPER_PERSONAS:
            raise HTTPException(
                status_code=400,
                detail=f"Persona '{persona_B_id}' no encontrada"
            )
        persona_B = RAPPER_PERSONAS[persona_B_id].copy()
        # Si se envía style_description desde el frontend, usarlo en lugar del del backend
        if style_description_B:
            persona_B["style_description"] = style_description_B

    rapper_A = RapperAgent("A", persona_A_id, persona_A, description_A if persona_A_id != "custom" else None)
    rapper_B = RapperAgent("B", persona_B_id, persona_B, description_B if persona_B_id != "custom" else None)

    rhyme_agent = RhymeMetricAgent()
    sentiment_agent = SentimentAttackAgent()
    moderation_agent = ModerationAgent()
    judge_agent = JudgeAgent()

    engine = BattleEngine(
        rapper_A=rapper_A,
        rapper_B=rapper_B,
        rhyme_agent=rhyme_agent,
        sentiment_agent=sentiment_agent,
        moderation_agent=moderation_agent,
        judge_agent=judge_agent,
        rounds=rounds,
    )

    return engine


def convert_battle_result_to_schema(result: BattleResult) -> BattleResultSchema:
    """Convierte BattleResult (dataclass) a BattleResultSchema (Pydantic)"""
    rounds_schema = []
    for round_result in result.rounds:
        verse_A_schema = VerseSchema(
            rapper_id=round_result.verse_A.rapper_id,
            round_number=round_result.verse_A.round_number,
            persona_id=round_result.verse_A.persona_id,
            text=round_result.verse_A.text,
        )
        verse_B_schema = VerseSchema(
            rapper_id=round_result.verse_B.rapper_id,
            round_number=round_result.verse_B.round_number,
            persona_id=round_result.verse_B.persona_id,
            text=round_result.verse_B.text,
        )
        round_schema = RoundResultSchema(
            round_number=round_result.round_number,
            score_A=round_result.score_A,
            score_B=round_result.score_B,
            winner=round_result.winner,
            verse_A=verse_A_schema,
            verse_B=verse_B_schema,
        )
        rounds_schema.append(round_schema)

    return BattleResultSchema(
        topic=result.topic,
        rounds=rounds_schema,
        overall_winner=result.overall_winner,
    )


@app.get("/", response_model=HealthResponse)
async def root():
    """Endpoint raíz - Health check"""
    return HealthResponse(
        status="ok",
        message="Rap Battle Arena API está funcionando"
    )


@app.get("/health", response_model=HealthResponse)
async def health():
    """Health check endpoint"""
    return HealthResponse(
        status="ok",
        message="API está funcionando correctamente"
    )


@app.get("/personas", response_model=PersonasResponse)
async def get_personas():
    """Obtiene todas las personalidades de raperos disponibles"""
    personas_list = [
        PersonaInfo(
            id=persona_id,
            name=persona["name"],
            language=persona["language"],
            flow_speed=persona["flow_speed"],
            aggressiveness=persona["aggressiveness"],
            complexity=persona["complexity"],
            style_description=persona["style_description"],
        )
        for persona_id, persona in RAPPER_PERSONAS.items()
    ]
    return PersonasResponse(personas=personas_list)


@app.post("/battle", response_model=BattleResultSchema)
async def start_battle(request: BattleRequest):
    """
    Inicia una nueva batalla de rap entre dos raperos virtuales.
    
    - **topic**: Tema de la batalla
    - **persona_A**: ID de la personalidad del rapero A
    - **persona_B**: ID de la personalidad del rapero B
    - **rounds**: Número de rondas (1-10)
    """
    try:
        # Normalize empty strings to None
        style_description_A = request.style_description_A.strip() if request.style_description_A and request.style_description_A.strip() else None
        style_description_B = request.style_description_B.strip() if request.style_description_B and request.style_description_B.strip() else None
        description_A = request.description_A.strip() if request.description_A and request.description_A.strip() else None
        description_B = request.description_B.strip() if request.description_B and request.description_B.strip() else None
        
        engine = create_battle_engine(
            persona_A_id=request.persona_A,
            persona_B_id=request.persona_B,
            rounds=request.rounds,
            style_description_A=style_description_A,
            style_description_B=style_description_B,
            description_A=description_A,
            description_B=description_B,
        )

        host = HostAgent(engine)
        result = host.start_battle(request.topic)

        return convert_battle_result_to_schema(result)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al ejecutar la batalla: {str(e)}"
        )


@app.get("/personas/{persona_id}", response_model=PersonaInfo)
async def get_persona(persona_id: str):
    """Obtiene información de una personalidad específica"""
    if persona_id not in RAPPER_PERSONAS:
        raise HTTPException(
            status_code=404,
            detail=f"Persona '{persona_id}' no encontrada"
        )

    persona = RAPPER_PERSONAS[persona_id]
    return PersonaInfo(
        id=persona_id,
        name=persona["name"],
        language=persona["language"],
        flow_speed=persona["flow_speed"],
        aggressiveness=persona["aggressiveness"],
        complexity=persona["complexity"],
        style_description=persona["style_description"],
    )

