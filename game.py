import sys
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

    def use_move(self, player: Player, creature: Creature):
        choice = 0
        movenames = [move.get_name() for move in player.moves if move.can_use()]
        choice = text.prompt_valid_choice(
            preamble="What move would you like to use?",
            options=movenames + ["Run"],
            prompt="Enter option: ")
        if choice == len(player.moves):
            print(text.flee_report("You"))
            return "flee", "flee"

        damage = -(player.get_attack() * player.moves[choice].get_multiplier())
        creature.change_hp(damage)
        player.moves[choice].used_moves()
        return player.moves[choice], damage

    def battle(self, player: Player, creature: Creature):
        print("You have entered a battle!\n")

        while creature.hp > 0:
            print(text.creature_report(
                name=creature.get_name(),
                hp=creature.get_hp(),
                attack=creature.get_attack()
            ))
            print(text.player_report(
                name="You",
                hp=player.get_hp(),
            ))
            used_move, damage = self.use_move(player, creature)
            if used_move == "flee":
                creature.change_hp(creature.maxhp)
                return False
            print(text.attack_report(
                name=player.get_name(),
                move=used_move.get_name(),
                damage=-int(damage),
            ))
            if creature.hp <= 0:
                break
            else:
                print(text.attack_report(
                    name=creature.get_name(),
                    move=creature.get_move_dropped(),
                    damage=creature.get_attack()
                ))
                player.change_hp(-creature.get_attack())
                if player.hp <= 0:
                    return False
        print(text.battle_report(
            victor="You",
            loser=creature.get_name(),
            loot=creature.get_move_dropped()
        ))
        player.moves.append(create_move(text.moves, creature.get_move_dropped()))
        return True

    def monster_battle(self, player: Player, monster: Monster):
        print(text.final_battle_report("You"))

        while monster.hp > 0:
            print(text.creature_report(
                name=monster.get_name(),
                hp=monster.get_hp(),
                attack=monster.get_attack()
            ))
            print(text.player_report(
                name="You",
                hp=player.get_hp(),
            ))
            used_move, damage = self.use_move(player, monster)
            if used_move == "flee":
                print(text.flee_report("You", fatal=True))
                player.hp = 0
                return
            print(text.attack_report(
                name=player.get_name(),
                move=used_move.get_name(),
                damage=-int(damage)
            ))
            if monster.hp <= 0:
                print(text.win_report("You"))
                sys.exit(0)
            else:
                print(text.monster_attack_report(
                    name=monster.get_name(),
                    damage=monster.get_attack()
                ))
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
            print(text.leave_gym_report("You"))
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
