from character import Character
from moves import Move


class Creature(Character):

    def __init__(self, name, hp: int, attack: int, move_dropped: str):
        super().__init__(name, hp, attack)
        self.move = Move(name=move_dropped, multiplier=1, power_limit=0)

    def get_move(self) -> Move:
        return self.move
