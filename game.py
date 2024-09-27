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
        monsteroptions = [
            f"{creature.get_name()} ({creature.get_hp()}HP, {creature.get_attack()} attack)"
            for creature in self.creatures
        ]
        choice = text.prompt_valid_choice(
            preamble="",
            options=monsteroptions + ["Go back"],
            prompt="Which Pokemon would you like to battle: ")
        if choice < len(monsteroptions):
            self.turns_to_monster -= 1
            won = self.creatures[choice].battle(player)
            if won:
                self.creatures.pop(choice)
        elif choice == len(monsteroptions):
            print("You left the gym...")
            return

    def options(self):
        return text.option_stack.copy()

    # def option_input(self):
    #     choice = input("Enter an option: ")
    #     return choice

    # def select_option(self, opt):
    #     self.choice = opt

    def do(self, player, choice):
        if choice in ['1', '2', '3', '4', '5', '6']:
            print(text.choice_stack[int(choice) - 1])
            if choice == "1":
                self.exercise(player)
                player.display_stats()
                self.turns_to_monster -= 1
            elif choice == "2":
                self.eat(player)
                player.display_stats()
                self.turns_to_monster -= 1
            elif choice == "3":
                self.sleep(player)
                player.display_stats()
                self.turns_to_monster -= 1
            elif choice == "6":
                self.gym(player)
            elif choice == "4":
                player.display_stats()
            elif choice == "5":
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
