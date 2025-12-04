from core.models import Verse
from typing import Tuple


class ModerationAgent:
    """
    Aplica una penalización si encuentra palabras prohibidas.
    No censuremos fuerte aquí, pero sí evita cosas muy agresivas o discriminatorias.
    """

    BANNED_WORDS = [
        "tonte", "estúpido", "idiota", "imbécil",
        "discriminacion",
    ]

    def analyze(self, verse: Verse) -> Tuple[float, bool]:
        text = verse.text.lower()
        penalty = 0.0
        is_allowed = True

        for bw in self.BANNED_WORDS:
            if bw and bw in text:
                penalty += 0.5  
                is_allowed = False

        penalty = min(penalty, 1.0)
        return penalty, is_allowed
