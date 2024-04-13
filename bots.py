from GameState import GameState
import random


def get_legal_moves(game: GameState) -> list[tuple[int]]:
    legal_moves = []
    for pile_idx, num_stones in enumerate(game.piles):
        legal_moves.extend((pile_idx, i) for i in range(1, num_stones+1))
    return legal_moves


def random_bot(game: GameState) -> tuple[int]:
    """
    Returns a random legal move
    """
    return random.choice(get_legal_moves(game))
