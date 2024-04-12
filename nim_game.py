"""
This is the main file for the game of Nim
"""
from GameState import GameState


def main():
    piles = [1, 2]
    game = GameState(piles)
    print(game)


if __name__ == "__main__":
    main()
