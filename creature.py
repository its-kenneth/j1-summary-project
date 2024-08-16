from character import Character

class Creature(Character):
    def __init__(self, name, hp, attack, move_dropped):
        super().__init__(name, hp, attack)
        self.move_dropped = move_dropped
            
    
    def battle(self, player):
        while self.hp >= 0:
            player.use_move()
            player.change_hp(-self.get_attack())

        
        