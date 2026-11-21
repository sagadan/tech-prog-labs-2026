from .damage import Damage
from .damage_handler import DamageHandler


class ArmorHandler(DamageHandler):
    def __init__(self, defense: float) -> None:
        super().__init__()
        self._defense = defense

    def handle(self, damage: Damage) -> None:
        damage.reduce_to(max(1, round(damage.amount * (1 - self._defense))))
        self._pass_to_next(damage)