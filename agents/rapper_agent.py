from typing import Optional, Dict
from core.models import Verse
from api.llm_client import generate_verse_llm


class RapperAgent:
    def __init__(self, rapper_id: str, persona_id: str, persona_config: Dict, additional_description: Optional[str] = None):
        self.rapper_id = rapper_id  
        self.persona_id = persona_id
        self.persona_config = persona_config
        self.additional_description = additional_description

    def generate_verse(
        self,
        round_number: int,
        topic: str,
        last_opponent_verse: Optional[str] = None,
    ) -> Verse:
        """
        Genera un verso para la ronda usando AWS Bedrock (LLM).
        """
        text = generate_verse_llm(
            persona=self.persona_config,
            topic=topic,
            last_opponent_verse=last_opponent_verse,
            additional_description=self.additional_description,
            max_lines=4,
            max_words_per_line=11,
        )

        return Verse(
            rapper_id=self.rapper_id,
            round_number=round_number,
            persona_id=self.persona_id,
            text=text,
        )
