"""
This is the main file for the game of Nim
"""
from GameState import GameState


def get_move_from_user(game: GameState) -> tuple[int]:
    '''
    Asks the user for input until they have given a valid move
    Returns (m, n)
    '''
    while True:
        try:
            s1 = f"Enter pile number (1-{len(game.piles)}): "
            pile_idx = int(input(s1)) - 1
            if 0 <= pile_idx < len(game.piles) and game.piles[pile_idx] > 0:
                break
            else:
                print("Invalid pile number. Choose a valid pile.")
        except ValueError:
            print("Invalid input. Please enter a valid pile number.")

    while True:
        try:
            s2 = f"Enter number of stones to take (1-{game.piles[pile_idx]}): "
            objects_to_remove = int(input(s2))
            if 1 <= objects_to_remove <= game.piles[pile_idx]:
                break
            else:
                print("Invalid number of objects. Choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return (pile_idx, objects_to_remove)


def two_player_nim(piles: list[int]) -> int:
    """
    Runs a single game of nim between two players.
    Returns the winning player (in [1, 2])
    """
    game = GameState(piles)
    player = 1
    while True:
        print(game)
        print(f"Player {player}'s turn...")
        m, n = get_move_from_user(game)
        game.make_move(m, n)

        if game.is_empty():
            print("It ended!")
            break
        else:
            player = 3 - player
    print("Game Over.")
    print(f"Player {player} wins!")
    return player


def main():
    two_player_nim([5, 5])


if __name__ == "__main__":
    main()
