from player import Player
import sys
import random

class Game:
    def __init__(self):
        self.turns_to_monster = 10

    def start(self, player):
        player.set_name()

    def display_options(self): # change later
        self.choice = input("""
What would you like to do?
1. Exercise
2. Eat
3. Sleep 
4. Display Stats
Enter option: """)

    def do(self, player): # changer later also
        if self.choice == "1":
            print("you exercised")
            self.exercise(player)
            self.turns_to_monster -= 1
        elif self.choice == "2":
            print("you eat")
            self.eat(player)
            self.turns_to_monster -= 1
        elif self.choice == "3":
            print("you slept")
            self.exercise(player)
            self.turns_to_monster -= 1
        elif self.choice == "4":
            player.display_stats()
        else:
            print("invalid choice")
            self.display_options()

        if self.turns_to_monster == 0:
            self.final_battle()

    def final_battle(self):
        while 
        sys.exit(0)

    def game_over(self, player):
        return player.get_hp() <= 0

    def exercise(self, player):
        player.change_attack(10)

    def sleep(self, player):
        player.recharge_hp(0.5)

    def eat(self, player):
        player.increase_hp(10)