from game import Game
from player import Player

if __name__ == "__main__":
    player = Player()
    game = Game()
    #monster = Monster()
    game.start(player)

    while not game.game_over(player):
        game.display_options()
        game.option_input()
        game.do(player)

    print("Died")