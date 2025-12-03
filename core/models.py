# core/models.py
from dataclasses import dataclass
from typing import List, Optional, Dict


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
        """Calculate total score based on weighted components"""
        if weights is None:
            weights = {
                "rhyme": 0.30,
                "metric": 0.20,
                "attack": 0.40,
                "sentiment": 0.05,
                "penalty": 0.20,
            }
        
        total = (
            self.rhyme_score * weights.get('rhyme', 0.25) +
            self.metric_score * weights.get('metric', 0.20) +
            self.attack_score * weights.get('attack', 0.25) +
            self.sentiment_score * weights.get('sentiment', 0.20) +
            self.penalty_score * weights.get('penalty', -0.10)
        )
        
        return max(0.0, total)  


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
