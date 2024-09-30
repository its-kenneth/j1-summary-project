from character import Character
import moves
from moves import Move


class Creature(Character):

    def __init__(self, name, hp: int, attack: int, move_dropped: str):
        super().__init__(name, hp, attack)
        self.move = moves.CharacterMove(name=move_dropped, multiplier=1, power_limit=0)

    def get_move(self) -> moves.CharacterMove:
        return self.move
