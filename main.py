from game import Game
from player import Player

if __name__ == "__main__":
    choice = 'y'

    while choice.lower() == 'y':
        player = Player()
        game = Game()
        game.start(player)

        while not game.game_over(player):
            game.display_options()
            game.option_input()
            game.do(player)

        choice = input("You died! Play again? (y/n): ")

    print("Thank you for playing!")
