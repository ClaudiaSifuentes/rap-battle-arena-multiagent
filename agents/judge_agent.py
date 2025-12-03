from core.models import AnalysisResult, RoundResult, Verse


class JudgeAgent:
    def __init__(self):
        self.default_weights = None

    def judge_round(
        self,
        round_number: int,
        analysis_A: AnalysisResult,
        analysis_B: AnalysisResult,
        verse_A: Verse,         
        verse_B: Verse,        
    ) -> RoundResult:
        score_A = analysis_A.total_score(self.default_weights)
        score_B = analysis_B.total_score(self.default_weights)

        if abs(score_A - score_B) < 0.05:
            winner = "draw"
        elif score_A > score_B:
            winner = "A"
        else:
            winner = "B"

        return RoundResult(
            round_number=round_number,
            score_A=score_A,
            score_B=score_B,
            winner=winner,
            verse_A=verse_A,    
            verse_B=verse_B,    # << NUEVO
        )
