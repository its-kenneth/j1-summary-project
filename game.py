import sys
import text
from creature import Creature
from monster import Monster

def create_monster():
    return Monster(text.monster["name"], text.monster["hp"], text.monster["attack"])

class Game:
    def __init__(self):
        self.turns_to_monster = 30

    def create_creature(self):
        for creature in text.creatures:
            self.creatures.append(Creature(creature["name"], creature["hp"], creature["attack"], creature["move_dropped"]))

    def start(self, player):
        player.set_name()
        self.creatures = []
        self.create_creature()
        
    def gym(self, player):
        for i in range(len(self.creatures)):
            print(f"{i + 1}: {self.creatures[i].get_name()}")
        print("4. Go back")
        battle_choice = input("Which Pokemon would you like to battle: ")
        if battle_choice in "123":
            self.turns_to_monster -= 1
            self.creatures[int(battle_choice) - 1].battle(player)
        elif battle_choice == '4':
            print("You left the gym...")
            return
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
    
    def do(self, player):
        if self.choice in "123456":
            print(text.choice_stack[int(self.choice)-1])
            if self.choice == "1":
                self.exercise(player)
                player.display_stats() 
                self.turns_to_monster -= 1
            elif self.choice == "2":
                self.eat(player)
                player.display_stats() 
                self.turns_to_monster -= 1
            elif self.choice == "3":
                self.sleep(player)
                player.display_stats() 
                self.turns_to_monster -= 1
            elif self.choice == "6":
                self.gym(player)
            elif self.choice == "4":
                player.display_stats() 
            elif self.choice == "5":
                player.display_moves()
            print()
        else:
            print("invalid choice \n")

        if self.turns_to_monster == 0:
            self.final_battle(player)

    def final_battle(self, player):
        monster = create_monster()
        monster.battle(player)

    def game_over(self, player):
        return player.get_hp() <= 0

    def exercise(self, player):
        player.change_attack(10)

    def sleep(self, player):
        player.sleep()

    def eat(self, player):
        player.increase_hp(10)