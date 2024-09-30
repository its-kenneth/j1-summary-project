import sys
import text
from creature import Creature
from monster import Monster
from moves import Move
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

    # def use_move(self, player: Player, creature: Creature):
    #     choice = 0
    #     movenames = [move.get_name() for move in player.moves if move.can_use()]
    #     choice = text.prompt_valid_choice(
    #         preamble="What move would you like to use?",
    #         options=movenames + ["Run"],
    #         prompt="Enter option: ")
    #     if choice == len(player.moves):
    #         print(text.flee_report("You"))
    #         return "flee", "flee"

    #     damage = -(player.get_attack() * player.moves[choice].get_multiplier())
    #     creature.change_hp(damage)
    #     player.moves[choice].used_moves()
    #     return player.moves[choice], damage

    def choose_move(self, character: Player | Creature | Monster) -> Move:
        """Have character select a move to use, and return the selected move."""
        if isinstance(character, Player):
            choice = 0
            movenames = [move.get_name() for move in character.moves if move.can_use()]
            choice = text.prompt_valid_choice(
                preamble="What move would you like to use?",
                options=movenames + ["Run"],
                prompt="Enter option: "
            )
            return character.moves[choice]
        elif isinstance(character, Creature):
            return character.get_move()
        elif isinstance(character, Monster):
            return character.get_move()

    def attack(
            self,
            attacker: Character,
            move: Move,
            defender: Character
        ) -> int:
        """Applies the effect of attacker using a move on the defender.
        Returns the damage dealt to defender.
        """
        if isinstance(attacker, Player):
            assert isinstance(move, Move)
            damage = -(attacker.get_attack() * move.get_multiplier())
            defender.change_hp(damage)
            move.used_moves()
            return damage
        elif isinstance(attacker, Creature | Monster):
            damage = -attacker.get_attack()
            defender.change_hp(damage)
            return damage
        raise TypeError(f"{attacker}: invalid attacker type")

    def battle(self, player: Player, enemy: Creature | Monster):
        if isinstance(enemy, Creature):
            print(text.battle_report("You"))
        elif isinstance(enemy, Monster):
            print(text.battle_report("You"), final=True)

        while not enemy.is_dead():
            print(text.creature_report(
                name=enemy.get_name(),
                hp=enemy.get_hp(),
                attack=enemy.get_attack()
            ))
            print(text.player_report(
                name="You",
                hp=player.get_hp(),
            ))
            move = self.choose_move(player)
            damage = self.attack(player, move, enemy)
            if move == "flee":
                if isinstance(enemy, Creature):
                    print(text.flee_report("You"))
                    creature.change_hp(creature.maxhp)
                    return False
                elif isinstance(enemy, Monster):
                    print(text.flee_report("You", fatal=True))
                    player.hp = 0
                    return False
            print(text.attack_report(
                name=player.get_name(),
                move=move.get_name(),
                damage=-int(damage),
            ))
            # If enemy killed
            if enemy.is_dead():
                if isinstance(enemy, Creature):
                    break
                if isinstance(enemy, Monster):
                    print(text.win_report("You"))
                    sys.exit(0)

            # Continue battle
            move = self.choose_move(enemy)
            damage = self.attack(enemy, move, player)
            if isinstance(enemy, Creature):
                print(text.attack_report(
                    name=enemy.get_name(),
                    move=enemy.get_move().name,
                    damage=enemy.get_attack()
                ))
                # player.change_hp(-enemy.get_attack())
            else:
                print(text.monster_attack_report(
                    name=enemy.get_name(),
                    damage=enemy.get_attack()
                ))
                # player.change_hp(-enemy.get_attack())
            if player.is_dead():
                return False
        return True

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
                print(text.battle_report(
                    victor="You",
                    loser=creature.get_name(),
                    loot=creature.get_move().name
                ))
                player.add_move(creature.get_move())
                self.creatures.pop(choice)
        elif choice == len(monsteroptions):
            print(text.leave_gym_report("You"))
            return

    def options(self):
        return list(text.choices.keys())

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
        self.battle(player, monster)

    def game_over(self, player):
        return player.is_dead()

    def exercise(self, player):
        player.change_attack(10)

    def sleep(self, player):
        self.restore_hp(player)
        self.restore_pp(player)

    def eat(self, player):
        player.increase_hp(15)
