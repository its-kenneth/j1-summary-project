import sys
import text
from creature import Creature

class Game:
    def __init__(self):
        self.turns_to_monster = 10

    def create_creature(self):
        for creature in text.creatures:
            self.creatures.append(Creature(creature["name"], creature["hp"], creature["attack"], creature["move_dropped"]))

    def start(self, player):
        player.set_name()
        self.creatures = []
        self.create_creature()

    def gym(self, player):
        for i in range(len(self.creatures)):
            print(f"{i + 1}:{self.creatures[i].get_name()}")
        battle_choice = input("Which Pokemon would you like to battle?\n")
        if battle_choice in "123":
            self.creatures[int(battle_choice) - 1].battle(player)
        else:
            print("Invalid choice")
            self.gym(player)
            
    def display_options(self): # change later
        print(f"Turns to monster: {self.turns_to_monster}")
        for i in range(len(text.option_stack)):
            print(f"{i+1}. {text.option_stack[i]}")
        
    def option_input(self):
        option = input("Enter an option: ")
        self.select_option(option)
        
    def select_option(self,opt):
        self.choice = opt
    
    def do(self, player): # changer later also
        if self.choice in "123456":
            print(text.choice_stack[int(self.choice)-1])
            if self.choice == "1":
                self.exercise(player)
                self.turns_to_monster -= 1
            elif self.choice == "2":
                self.eat(player)
                self.turns_to_monster -= 1
            elif self.choice == "3":
                self.sleep(player)
                self.turns_to_monster -= 1
            elif self.choice == "6":
                self.gym(player) #@Manuel
                self.turns_to_monster -= 1
            elif self.choice == "4":
                player.display_stats() 
            elif self.choice == "5":
                player.display_moves() #@Manuel
            print()
        else:
            print("invalid choice \n")

        if self.turns_to_monster == 0:
            self.final_battle()

    def final_battle(self):
        print("you fought and won")
        sys.exit(0)

    def game_over(self, player):
        return player.get_hp() <= 0

    def exercise(self, player):
        player.change_attack(10)

    def sleep(self, player):
        player.recharge_hp(0.5)

    def eat(self, player):
        player.increase_hp(10)