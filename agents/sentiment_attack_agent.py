from core.models import Verse
from typing import Tuple


class SentimentAttackAgent:
    """
    Aproximación simple:
    - attack_score: proporción de palabras 'de ataque'
    - sentiment_score: heurístico (+0.5 si hay ataque, 0 en caso contrario)
    """

    ATTACK_WORDS = [
        "débil", "falso", "malo", "pierdes", "fracaso",
        "mediocre", "ridículo", "payaso", "parásito",
        "amateur", "hund", "aplast", "derrib", "sin aliento",
        "te destruyo", "te derrumbo", "te hunden",
        "soy el amo", "domino este escenario",
    ]
    
    def analyze(self, verse: Verse) -> Tuple[float, float]:
        text = verse.text.lower()
        words = [w for w in text.replace("\n", " ").split() if w]
        if not words:
            return 0.0, 0.0

        total_words = len(words)
        attack_hits = 0

        for w in words:
            for aw in self.ATTACK_WORDS:
                if aw in w:
                    attack_hits += 1
                    break

        attack_score = attack_hits / total_words

        sentiment_score = 0.5 if attack_hits > 0 else 0.0

        return sentiment_score, attack_score
