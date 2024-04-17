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
