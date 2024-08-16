from character import Character
from text import moves
from player import create_move

class Creature(Character):
    def __init__(self, name, hp, attack, move_dropped):
        super().__init__(name, hp, attack)
        self.move_dropped = move_dropped
            
    def get_move_dropped(self):
        return self.move_dropped
    
    def battle(self, player):
        while self.hp >= 0:
            player.use_move()
            player.change_hp(-self.get_attack())

        print(f"You won! {self.get_name()} dropped {self.get_move_dropped()}")
        player.moves.append(create_move(moves, self.get_move_dropped()))

        
        