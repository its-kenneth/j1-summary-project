import text
from moves import Move
from character import Character


def create_move(moves, name) -> Move:
    for move in moves:
        if move["name"] == name:
            return Move(move["name"], move["multiplier"], move["power_limit"])
    raise ValueError(f"Move {name} not found")


class Player(Character):

    def __init__(self):
        super().__init__()
        self.moves = [create_move(text.moves, "Kick")]

    def add_move(self, move: Move):
        self.moves.append(move)

    def set_name(self):
        self.name = input("Enter the name of user: ")

    def display_stats(self):
        print(f"HP: {self.hp}/{self.maxhp}")
        print(f"Attack: {self.attack}")

    def display_moves(self):
        for move in self.moves:
            print(f"""Name: {move.get_name()}
Multiplier: {move.get_multiplier()}
PP: {move.get_current_power()}/{move.get_power_limit()}
""")
        print()
