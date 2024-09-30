from character import Character


class Monster(Character):
    def __init__(self, name, hp: int, attack: int):
        super().__init__(name, hp, attack)
        self.move = Move(name="Lash", multiplier=1, power_limit=0)

    def get_move(self) -> Move:
        return self.move
