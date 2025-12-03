from personas.personas import RAPPER_PERSONAS
from agents.rapper_agent import RapperAgent
from agents.rhyme_metric_agent import RhymeMetricAgent
from agents.sentiment_attack_agent import SentimentAttackAgent
from agents.moderation_agent import ModerationAgent
from agents.judge_agent import JudgeAgent
from agents.host_agent import HostAgent
from core.battle_engine import BattleEngine


def main():
    topic = "Quién domina más el escenario"

    # Crear raperos con personalidades diferentes
    persona_A = RAPPER_PERSONAS["fast_technical"]
    persona_B = RAPPER_PERSONAS["punchline_master"]

    rapper_A = RapperAgent("A", "fast_technical", persona_A)
    rapper_B = RapperAgent("B", "punchline_master", persona_B)

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
        rounds=3,
    )

    host = HostAgent(engine)
    result = host.start_battle(topic)

    print(f"TEMA: {result.topic}")
    print("=" * 60)

    for r in result.rounds:
        print(f"\nRonda {r.round_number} → Ganador: {r.winner}")
        print(f"  Score A: {r.score_A:.3f}")
        print(f"  Score B: {r.score_B:.3f}")
        print("-" * 60)
        print("[Rapero A]")
        print(r.verse_A.text)
        print("\n[Rapero B]")
        print(r.verse_B.text)
        print("\n" + "-" * 60)

    print(f"\nGANADOR GLOBAL: {result.overall_winner}")


if __name__ == "__main__":
    main()
