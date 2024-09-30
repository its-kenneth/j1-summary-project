import sys
import text
from creature import Creature
from monster import Monster
import moves
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

    def choose_move(self, character: Player | Creature | Monster) -> moves.Move:
        """Have character select a move to use, and return the selected move."""
        if isinstance(character, Player):
            choice = 0
            movenames = [move.get_name() for move in character.moves if move.can_use()]
            choice = text.prompt_valid_choice(
                preamble="What move would you like to use?",
                options=movenames + ["Run"],
                prompt="Enter option: "
            )
            if choice == len(movenames):
                return Flee()
            else:
                return character.moves[choice]
        elif isinstance(character, Creature):
            return character.get_move()
        elif isinstance(character, Monster):
            return character.get_move()

    def attack(
            self,
            attacker: Character,
            move: moves.CharacterMove,
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

        attacker, defender = player, enemy
        while not attacker.is_dead():
            if isinstance(attacker, Player):
                print(text.creature_report(
                    name=defender.get_name(),
                    hp=defender.get_hp(),
                    attack=defender.get_attack()
                ))
                print(text.player_report(
                    name="You",
                    hp=attacker.get_hp(),
                ))
            move = self.choose_move(attacker)
            damage = self.attack(attacker, move, defender)
            if isinstance(move, moves.Flee):  # assume only player can flee
                if isinstance(defender, Creature):
                    print(text.flee_report("You"))
                    defender.change_hp(defender.maxhp)
                    return False
                elif isinstance(defender, Monster):
                    print(text.flee_report("You", fatal=True))
                    player.hp = 0
                    return False
            if isinstance(attacker, Player):
                print(text.attack_report(
                    name=attacker.get_name(),
                    move=move.get_name(),
                    damage=-int(damage),
                ))
            elif isinstance(attacker, Creature):
                print(text.attack_report(
                    name=attacker.get_name(),
                    move=move.get_name(),
                    damage=-int(damage)
                ))
            elif isinstance(attacker, Monster):
                print(text.monster_attack_report(
                    name=attacker.get_name(),
                    damage=-int(damage)
                ))

            # If attacker or defender killed
            if defender.is_dead():
                if isinstance(defender, Creature):
                    break
                if isinstance(defender, Monster):
                    print(text.win_report("You"))
                    sys.exit(0)
            elif player.is_dead():
                return False
            attacker, defender = defender, attacker
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
