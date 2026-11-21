from ..combat.combatant import Combatant
from .action import Action
from .tactic import Tactic


class AggressiveTactic(Tactic):
    @property
    def code(self) -> str:
        return "aggressive"

    @property
    def display_name(self) -> str:
        return "Натиск"

    @property
    def description(self) -> str:
        return "безрассудные удары, пока у врага больше здоровья"

    def choose_action(self, round: int, hero: Combatant, enemy: Combatant) -> Action:
        return Action.POWER_STRIKE if enemy.health > hero.health else Action.ATTACK