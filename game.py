import text
from creature import Creature
from monster import Monster


def create_monster():
    return Monster(text.monster["name"], text.monster["hp"],
                   text.monster["attack"])


class Game:

    def __init__(self):
        self.turns_to_monster = 30

    def create_creature(self):
        for creature in text.creatures:
            self.creatures.append(
                Creature(creature["name"], creature["hp"], creature["attack"],
                         creature["move_dropped"]))

    def start(self, player):
        text.intro()
        player.set_name()
        self.creatures = []
        self.create_creature()

    def gym(self, player):
        for i in range(len(self.creatures)):
            print(
                f"{i + 1}: {self.creatures[i].get_name()} ({self.creatures[i].get_hp()}HP, {self.creatures[i].get_attack()} attack)"
            )
        print(f"{len(self.creatures) + 1}. Go back")
        battle_choice = input("Which Pokemon would you like to battle: ")

        valid_input = []
        for i in range(1, len(self.creatures) + 1):
            valid_input.append(str(i))
        if battle_choice in valid_input:
            self.turns_to_monster -= 1
            won = self.creatures[int(battle_choice) - 1].battle(player)
            if won:
                self.creatures.pop(int(battle_choice) - 1)
        elif battle_choice == str(len(self.creatures) + 1):
            print("You left the gym...")
            return
        else:
            print("Invalid choice")
            self.gym(player)

    def display_options(self):  # change later
        print(f"Turns to monster: {self.turns_to_monster}")
        for i in range(len(text.option_stack)):
            print(f"{i+1}. {text.option_stack[i]}")

    def option_input(self):
        option = input("Enter an option: ")
        self.select_option(option)

    def select_option(self, opt):
        self.choice = opt

    def do(self, player):
        if self.choice in ['1', '2', '3', '4', '5', '6']:
            print(text.choice_stack[int(self.choice) - 1])
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
        player.increase_hp(15)
