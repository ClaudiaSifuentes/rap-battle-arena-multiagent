from core.models import Verse
import re
from typing import Tuple


class RhymeMetricAgent:
    """
    Analiza rima y métrica de un verso de forma aproximada.
    """

    VOWEL_PATTERN = re.compile(r"[aeiouáéíóúü]+", re.IGNORECASE)

    def analyze(self, verse: Verse) -> Tuple[float, float]:
        """
        Devuelve (rhyme_score, metric_score) en rango 0–1.
        """
        lines = [l.strip() for l in verse.text.split("\n") if l.strip()]
        if not lines:
            return 0.0, 0.0

        syllable_counts = []
        endings = []

        for line in lines:
            syllables = len(self.VOWEL_PATTERN.findall(line))
            syllable_counts.append(syllables)

            words = line.split()
            last_word = words[-1] if words else ""
            endings.append(last_word[-3:].lower())

        ideal_min, ideal_max = 8, 12
        metric_scores = []
        for s in syllable_counts:
            if s < ideal_min:
                diff = ideal_min - s
            elif s > ideal_max:
                diff = s - ideal_max
            else:
                diff = 0
            metric_scores.append(max(0.0, 1.0 - diff / 6.0))  

        metric_score = sum(metric_scores) / len(metric_scores)

        rhyme_score = 0.0
        if len(endings) > 1:
            counts = {}
            for e in endings:
                counts[e] = counts.get(e, 0) + 1
            max_group = max(counts.values())
            rhyme_score = max_group / len(endings)

        return rhyme_score, metric_score
