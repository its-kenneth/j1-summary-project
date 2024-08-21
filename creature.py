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
        print("You have entered a battle!\n")
        
        while self.hp > 0:
            print(f"{self.get_name()} has {int(self.get_hp())}HP left and {self.get_attack()} attack")
            print(f"You have {player.get_hp()}HP left.\n")
            
            used_move, damage = player.use_move(self)
            print()
            
            if used_move == "flee":
                self.change_hp(self.maxhp)
                return
                
            print(f"{player.get_name()} used {used_move.get_name()}! It dealt {-int(damage)} damage!")
            
            if self.hp <= 0:
                break
            else:
                print(f"{self.get_name()} used {self.get_move_dropped()}! It dealt {self.get_attack()} damage!\n")
                
                player.change_hp(-self.get_attack())
                if player.hp <= 0:
                    return

        print(f"You won! {self.get_name()} dropped {self.get_move_dropped()}")
        player.moves.append(create_move(moves, self.get_move_dropped()))
