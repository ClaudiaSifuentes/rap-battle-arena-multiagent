from typing import List
from core.models import BattleResult, AnalysisResult, Verse
from agents.rapper_agent import RapperAgent
from agents.rhyme_metric_agent import RhymeMetricAgent
from agents.sentiment_attack_agent import SentimentAttackAgent
from agents.moderation_agent import ModerationAgent
from agents.judge_agent import JudgeAgent


class BattleEngine:
    def __init__(
        self,
        rapper_A: RapperAgent,
        rapper_B: RapperAgent,
        rhyme_agent: RhymeMetricAgent,
        sentiment_agent: SentimentAttackAgent,
        moderation_agent: ModerationAgent,
        judge_agent: JudgeAgent,
        rounds: int = 3,
    ):
        self.rapper_A = rapper_A
        self.rapper_B = rapper_B
        self.rhyme_agent = rhyme_agent
        self.sentiment_agent = sentiment_agent
        self.moderation_agent = moderation_agent
        self.judge_agent = judge_agent
        self.rounds = rounds

    def run_battle(self, topic: str) -> BattleResult:
        round_results = []
        last_verse_A: Verse | None = None
        last_verse_B: Verse | None = None

        for r in range(1, self.rounds + 1):
            # Verso A
            verse_A = self.rapper_A.generate_verse(
                round_number=r,
                topic=topic,
                last_opponent_verse=last_verse_B.text if last_verse_B else None,
            )
            # Verso B
            verse_B = self.rapper_B.generate_verse(
                round_number=r,
                topic=topic,
                last_opponent_verse=last_verse_A.text if last_verse_A else None,
            )

            last_verse_A, last_verse_B = verse_A, verse_B

            # Análisis verso A
            rhyme_A, metric_A = self.rhyme_agent.analyze(verse_A)
            sentiment_A, attack_A = self.sentiment_agent.analyze(verse_A)
            penalty_A, _ = self.moderation_agent.analyze(verse_A)

            analysis_A = AnalysisResult(
                rhyme_score=rhyme_A,
                metric_score=metric_A,
                attack_score=attack_A,
                sentiment_score=sentiment_A,
                penalty_score=penalty_A,
            )

            # Análisis verso B
            rhyme_B, metric_B = self.rhyme_agent.analyze(verse_B)
            sentiment_B, attack_B = self.sentiment_agent.analyze(verse_B)
            penalty_B, _ = self.moderation_agent.analyze(verse_B)

            analysis_B = AnalysisResult(
                rhyme_score=rhyme_B,
                metric_score=metric_B,
                attack_score=attack_B,
                sentiment_score=sentiment_B,
                penalty_score=penalty_B,
            )

            # Juzgar ronda
            round_result = self.judge_agent.judge_round(
                round_number=r,
                analysis_A=analysis_A,
                analysis_B=analysis_B,
                verse_A=verse_A,      
                verse_B=verse_B,     
            )
            round_results.append(round_result)

        print(f"[DEBUG] Ronda {r} - Rapero A:")
        print(f"  rhyme={analysis_A.rhyme_score:.3f}, metric={analysis_A.metric_score:.3f}, "
            f"attack={analysis_A.attack_score:.3f}, sentiment={analysis_A.sentiment_score:.3f}, "
            f"penalty={analysis_A.penalty_score:.3f}")

        print(f"[DEBUG] Ronda {r} - Rapero B:")
        print(f"  rhyme={analysis_B.rhyme_score:.3f}, metric={analysis_B.metric_score:.3f}, "
            f"attack={analysis_B.attack_score:.3f}, sentiment={analysis_B.sentiment_score:.3f}, "
            f"penalty={analysis_B.penalty_score:.3f}")


        # Determinar ganador global
        score_A_total = sum(r.score_A for r in round_results)
        score_B_total = sum(r.score_B for r in round_results)

        if abs(score_A_total - score_B_total) < 0.05:
            overall_winner = "draw"
        elif score_A_total > score_B_total:
            overall_winner = "A"
        else:
            overall_winner = "B"

        return BattleResult(
            topic=topic,
            rounds=round_results,
            overall_winner=overall_winner,
        )
