from character import Character


class Creature(Character):

    def __init__(self, name, hp, attack, move_dropped):
        super().__init__(name, hp, attack)
        self.move_dropped = move_dropped

    def get_move_dropped(self):
        return self.move_dropped
