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
        self.moves = [create_move(moves, "Kick")]
    
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

    def sleep(self):
        self.change_hp(self.get_maxhp())
        for i in range(len(self.moves)):
            self.moves[i].set_current_power(self.moves[i].get_power_limit())
            

    def use_move(self, creature):
        choice = 0

        while choice <= 0 or choice > len(self.moves):
            print("What move would you like to use?")
            for i in range(len(self.moves)):
                print(f"{i+1}: ", end="")
                print(self.moves[i].get_name())
            print(f"{len(self.moves) + 1}: Run")
    
            choice = int(input("Enter option: "))
            if choice > 0 and choice <= len(self.moves):
                if not self.moves[choice - 1].can_use():
                    print("Move has no more PP!")
                    choice = 0
            elif choice == len(self.moves) + 1:
                print("You flee from the battle...")
                return "flee", "flee"
            else:
                print("Invalid option")

        damage = -(self.get_attack()*self.moves[choice - 1].get_multiplier())
        creature.change_hp(damage)
        self.moves[choice - 1].used_moves()
        return self.moves[choice - 1], damage