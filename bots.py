from GameState import GameState
import random


def get_legal_moves(game: GameState) -> list[tuple[int]]:
    """
    Returns a list of legal moves for a given game with syntax
        [(pile_idx, 1), (pile_idx, 2), ...]
    """
    legal_moves = []
    for pile_idx, num_stones in enumerate(game.piles):
        legal_moves.extend((pile_idx, i) for i in range(1, num_stones+1))
    return legal_moves


def random_bot(game: GameState) -> tuple[int]:
    """
    Returns a random legal move
    """
    return random.choice(get_legal_moves(game))


def two_pile_bot(game: GameState) -> tuple[int]:
    """
    If this bot plays in a game of two piles it will play optimally
    If there are more than two piles it will play randomly
    """
    p = game.piles
    nonempty_count = sum([1 if i > 0 else 0 for i in p])
    legal_moves = get_legal_moves(game)

    if nonempty_count > 2:
        return random_bot(game)
    elif nonempty_count == 1:
        # remove all the stones
        return max(legal_moves, key=lambda x: x[1])
    else:  # exactly two piles
        pile_ids = list(set([i for i, m in legal_moves]))
        pile1 = pile_ids[0]
        pile2 = pile_ids[1]
        a = p[pile1]
        b = p[pile2]

        if a == b:  # no winning strategy
            return (pile1, 1)
        elif a < b:
            return (pile2, b - a)
        elif a > b:
            return (pile1, a - b)
    return None


def nim_sum_bot(game: GameState) -> tuple[int]:
    """
    Plays optimally in a Nim game using the strategy based on nim-sum.
    """
    def calculate_nim_sum(piles):
        """
        Calculates the nim-sum (xor of all pile sizes) for a given game state.
        """
        nim_sum = 0
        for pile in piles:
            nim_sum ^= pile
        return nim_sum

    piles = game.piles
    nim_sum = calculate_nim_sum(piles)

    if nim_sum == 0:
        # If the nim-sum is zero, the position is losing for the current player
        # This means the opponent will win with optimal play
        # In this case, the bot can't win but must make a move
        # We'll choose to reduce any non-empty
        # pile to make the nim-sum non-zero
        for i in range(len(piles)):
            if piles[i] > 0:
                return i, 1  # Make a move that decreases the nim-sum
        return None  # This should not happen if the game is played correctly

    # Find a move that reduces a pile to the nim-sum of
    # its original size with nim_sum
    for i in range(len(piles)):
        current_nim_sum = piles[i] ^ nim_sum
        if current_nim_sum < piles[i]:
            stones_to_remove = piles[i] - current_nim_sum
            return i, stones_to_remove

    return None  # This should not happen if the game is played correctly
