import text
from creature import Creature
from monster import Monster
from player import Player, create_move


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

    def restore_hp(self, player: Player):
        player.change_hp(player.get_maxhp())

    def restore_pp(self, player: Player):
        for i in range(len(player.moves)):
            player.moves[i].set_current_power(player.moves[i].get_power_limit())

    def battle(self, player: Player, creature: Creature):
        print("You have entered a battle!\n")

        while creature.hp > 0:
            print(
                f"{creature.get_name()} has {int(creature.get_hp())}HP left and {creature.get_attack()} attack"
            )
            print(f"You have {player.get_hp()}HP left.\n")
            used_move, damage = player.use_move(self)
            print()
            if used_move == "flee":
                creature.change_hp(self.maxhp)
                return False
            print(
                f"{player.get_name()} used {used_move.get_name()}! It dealt {-int(damage)} damage!"
            )
            if creature.hp <= 0:
                break
            else:
                print(
                    f"{creature.get_name()} used {creature.get_move_dropped()}! It dealt {creature.get_attack()} damage!\n"
                )
                player.change_hp(-creature.get_attack())
                if player.hp <= 0:
                    return False
        print(f"You won! {creature.get_name()} dropped {creature.get_move_dropped()}")
        player.moves.append(create_move(text.moves, creature.get_move_dropped()))
        return True

    def monster_battle(self, player: Player, monster: Monster):
        print("You have entered the final battle!\n")

        while monster.hp > 0:
            print(
                f"{monster.get_name()} has {int(monster.get_hp())}HP left and {monster.get_attack()} attack"
            )
            print(f"You have {player.get_hp()}HP left.\n")

            used_move, damage = player.use_move(monster)
            print()

            if used_move == "flee":
                print(
                    "You coward! The monster struck a fatal blow as you were fleeing, causing you to bleed to death."
                )
                player.hp = 0
                return

            print(
                f"{player.get_name()} used {used_move.get_name()}! It dealt {-int(damage)} damage!"
            )

            if monster.hp <= 0:
                print("You won! Thank you for playing!")
                sys.exit(0)
            else:
                print(
                    f"{monster.get_name()} lashed out! It dealt {monster.get_attack()} damage!\n"
                )

                player.change_hp(-monster.get_attack())
                if player.hp <= 0:
                        return

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
            won = self.battle(player, self.creatures[choice])
            if won:
                self.creatures.pop(choice)
        elif choice == len(monsteroptions):
            print("You left the gym...")
            return

    def options(self):
        return list(text.choices.keys())

    # def option_input(self):
    #     choice = input("Enter an option: ")
    #     return choice

    # def select_option(self, opt):
    #     self.choice = opt

    def use_turns(self, n: int) -> None:
        """Use up n turns. n must be zero or positive."""
        if n < 0:
            raise ValueError("n must be zero or positive")
        if self.turns_to_monster <= n:
            raise ValueError("Not enough turns to use")
        self.turns_to_monster -= n

    def do(self, player, choice_label: str):
        if choice_label not in text.choices:
            raise ValueError(f"Choice {choice_label} not found")
        choice = text.choices[choice_label]
        print(choice.text)
        if choice.label == "Exercise":
            self.exercise(player)
            player.display_stats()
        elif choice.label == "Eat":
            self.eat(player)
            player.display_stats()
        elif choice.label == "Sleep":
            self.sleep(player)
            player.display_stats()
        elif choice.label == "Go to Pokemon Gym":
            self.gym(player)
        elif choice.label == "Display Stats":
            player.display_stats()
        elif choice.label == "Display Moves":
            player.display_moves()
        self.use_turns(choice.turns_used)

        if self.turns_to_monster == 0:
            self.final_battle(player)

    def final_battle(self, player):
        monster = create_monster()
        self.monster_battle(player, monster)

    def game_over(self, player):
        return player.get_hp() <= 0

    def exercise(self, player):
        player.change_attack(10)

    def sleep(self, player):
        self.restore_hp(player)
        self.restore_pp(player)

    def eat(self, player):
        player.increase_hp(15)
