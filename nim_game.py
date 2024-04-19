"""
This is the main file for the game of Nim
"""
from GameState import GameState
import bots


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


def two_player_nim(game: GameState) -> int:
    """
    Runs a single game of nim between two players.
    Returns the winning player (in [1, 2])
    """
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


def player_vs_bot_nim(game: GameState, user_first=True) -> int:
    """
    Runs a single game of nim between the user and computer
    User determins whether the user goes first or second
    Returns true iff the user wins
    """
    user_turn = user_first
    while True:
        print(game)
        if user_turn:
            print("Your turn...")
            m, n = get_move_from_user(game)
            game.make_move(m, n)
        else:
            # move = bots.random_bot(game)
            move = bots.two_pile_bot(game)
            m, n = move
            game.make_move(m, n)
            print(f"Computer takes {n} stones from pile {m+1}")

        if game.is_empty():
            print("It ended!")
            break
        else:
            user_turn = not user_turn
    print("Game Over.")
    if user_turn:
        print("You win!")
        return True
    else:
        print("You Lose!")
        return False


def bot_vs_bot_nim(game: GameState, bot1='random', bot2='random', verbose=True):
    """
    Runs a single game of nim betwen two bots
    The bot name must be in the list of valid bots
    Prints statements if verbose
    Returns true iff bot1 wins
    """
    # Define the bot functions based on their names
    def get_bot_function(bot_name):
        if bot_name == 'random':
            return bots.random_bot
        elif bot_name == 'two_pile':
            return bots.two_pile_bot
        elif bot_name == 'nim_sum':
            return bots.nim_sum_bot
        else:
            raise ValueError(f"Unknown bot: {bot_name}")

    bot1_function = get_bot_function(bot1)
    bot2_function = get_bot_function(bot2)

    current_bot = bot1_function
    next_bot = bot2_function

    while True:
        if verbose:
            print(game)

        # Determine the move based on the current bot
        move = current_bot(game)

        # Make the move
        m, n = move
        game.make_move(m, n)

        if verbose:
            print(f"{current_bot.__name__} takes {n} stones from pile {m + 1}")

        # Check if the game is over
        if game.is_empty():
            print("Game Over.")
            return current_bot == bot1_function  # bot1 wins if it's its turn

        # Swap bots for the next turn
        current_bot, next_bot = next_bot, current_bot


def main():
    # two_player_nim([5, 5])
    # player_vs_bot_nim([3, 4, 5])
    bot1 = 'nim_sum'
    bot2 = 'two_pile'
    outcome = bot_vs_bot_nim(GameState([3, 4, 5]), bot1, bot2, True)
    if outcome:
        print("Bot1:", bot1, "wins!")
    else:
        print("Bot2:", bot2, "wins!")


if __name__ == "__main__":
    main()
