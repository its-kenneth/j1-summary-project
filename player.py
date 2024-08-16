from text import moves
from moves import Move
from character import Character

def create_move(moves, name):
    for move in moves:
        if move["name"] == name:
            return Move(move["name"], move["multiplier"], move["power_limit"])

class Player(Character):
    def __init__(self):
        super().__init__()
        self.moves = [create_move(moves, "kick")]
    
    def set_name(self):
        self.name = input("Enter the name of user: ")
        
    def display_stats(self):
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack}")

    def recharge_hp(self,percentage):
        self.change_hp(self.hp * percentage)

    def use_move(self, creature):
        choice = 0

        while choice <= 0 or choice > len(self.moves):
            print("What move would you like to use?")
            for i in range(len(self.moves)):
                print(f"{i+1}: ", end="")
                print(self.moves[i].get_name())
    
            choice = int(input("Enter option: "))
            if choice > 0 and choice <= len(self.moves):
                break
            else:
                print("Invalid option")

        creature.change_hp(-(self.get_attack()*self.moves[choice].get_multiplier()))
        self.moves[choice].used_moves()
        
                
            
        
        