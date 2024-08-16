from player import Player
import sys
import random
import text

class Game:
    def __init__(self):
        
        self.turns_to_monster = 10

    def start(self, player):
        player.set_name()
    
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
        if self.choice in "1234":
            print(text.choice_stack[int(self.choice)-1])
            print()
            if self.choice in "123":
                self.turns_to_monster -= 1
            if self.choice == "4":
                player.display_stats()
        else:
            print("invalid choice")
            self.display_options()

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