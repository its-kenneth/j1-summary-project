from game import Game
from player import Player
import text

if __name__ == "__main__":
    choice = 'y'

    while choice.lower() == 'y':
        player = Player()
        game = Game()
        game.start(player)

        while not game.game_over(player):
            choice = text.prompt_player_choice(
                options=game.options(),
                preamble=f"Turns to monster: {game.turns_to_monster}",
                prompt="Enter an option: "
            )
            game.do(player, choice)

        choice = input("You died! Play again? (y/n): ")

    print("Thank you for playing!")
