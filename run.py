import pygame
from game.game_of_life import GameOfLife


def main():
    pygame.init()
    game_of_life = GameOfLife()
    game_of_life.run()


if __name__ == "__main__":
    main()
