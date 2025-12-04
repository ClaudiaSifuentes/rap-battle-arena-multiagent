# api/schemas.py
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional


class VerseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    rapper_id: str
    round_number: int
    persona_id: str
    text: str


class RoundResultSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    round_number: int
    score_A: float
    score_B: float
    winner: str
    verse_A: VerseSchema
    verse_B: VerseSchema


class BattleResultSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    topic: str
    rounds: List[RoundResultSchema]
    overall_winner: str


class BattleRequest(BaseModel):
    topic: str = Field(..., description="Tema de la batalla")
    persona_A: str = Field(
        default="fast_technical",
        description="ID de la personalidad del rapero A"
    )
    persona_B: str = Field(
        default="punchline_master",
        description="ID de la personalidad del rapero B"
    )
    rounds: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Número de rondas (1-10)"
    )
    style_description_A: Optional[str] = Field(
        default=None,
        description="Descripción de estilo del rapero A"
    )
    style_description_B: Optional[str] = Field(
        default=None,
        description="Descripción de estilo del rapero B"
    )
    description_A: Optional[str] = Field(
        default=None,
        description="Descripción adicional del rapero A"
    )
    description_B: Optional[str] = Field(
        default=None,
        description="Descripción adicional del rapero B"
    )


class PersonaInfo(BaseModel):
    id: str
    name: str
    language: str
    flow_speed: str
    aggressiveness: str
    complexity: str
    style_description: str


class PersonasResponse(BaseModel):
    personas: List[PersonaInfo]


class HealthResponse(BaseModel):
    status: str
    message: str

