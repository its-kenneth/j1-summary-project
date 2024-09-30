class Move:
    """Base class"""

class CharacterMove(Move):

    def __init__(self, name: str, multiplier: float, power_limit: int):
        self.name = name
        self.multiplier = multiplier
        self.power_limit = power_limit
        self.current_power = power_limit

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_multiplier(self) -> float:
        return self.multiplier

    def set_multiplier(self, multiplier):
        self.multiplier = multiplier

    def get_power_limit(self) -> int:
        return self.power_limit

    def set_power_limit(self, power_limit: int):
        self.power_limit = power_limit

    def get_current_power(self) -> int:
        return self.current_power

    def set_current_power(self, power: int):
        self.current_power = power

    def can_use(self) -> bool:
        return self.current_power > 0

    def used_moves(self) -> None:
        self.current_power -= 1


class Flee(Move):
    pass