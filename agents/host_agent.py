from core.battle_engine import BattleEngine
from core.models import BattleResult


class HostAgent:
    def __init__(self, engine: BattleEngine):
        self.engine = engine

    def start_battle(self, topic: str) -> BattleResult:
        """
        Orquesta la batalla completa mediante el BattleEngine.
        """
        result = self.engine.run_battle(topic)
        return result
