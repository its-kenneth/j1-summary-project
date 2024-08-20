from character import Character
import sys

class Monster(Character):
    def battle(self, player):
        print("You have entered the final battle!\n")

        while self.hp > 0:
            print(f"{self.get_name()} has {int(self.get_hp())}HP left and {self.get_attack()} attack")
            print(f"You have {player.get_hp()}HP left.\n")

            used_move, damage = player.use_move(self)
            print()

            if used_move == "flee":
                print("You coward! The monster struck a fatal blow as you were fleeing, causing you to bleed to death.")
                player.hp = 0
                return

            print(f"{player.get_name()} used {used_move.get_name()}! It dealt {-int(damage)} damage!")

            if self.hp <= 0:
                print("You won! Thank you for playing!")
                sys.exit(0)
            else:
                print(f"{self.get_name()} lashed out! It dealt {self.get_attack()} damage!\n")

                player.change_hp(-self.get_attack())
                if player.hp <= 0:
                    return