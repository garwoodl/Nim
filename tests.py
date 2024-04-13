from nim_game import GameState
from bots import get_legal_moves


def test_is_empty():
    game1 = GameState([0, 0, 0, 0, 0])
    game2 = GameState([0])
    game3 = GameState([1])
    assert game1.is_empty()
    assert game2.is_empty()
    assert not game3.is_empty()


def test_eq():
    game1 = GameState([1, 2, 3])
    game2 = GameState([1, 2, 3])
    game3 = GameState([1, 2])
    assert game1 == game2
    assert game1 != game3


def test_is_legal_move():
    pile1 = [0]
    pile2 = [0, 5]
    game1 = GameState(pile1)
    game2 = GameState(pile2)
    assert not game1.is_legal_move(0, 0)
    assert game2.is_legal_move(1, 5)
    assert not game2.is_legal_move(0, 1)


def test_make_move():
    pile1 = [1, 5, 3]
    game1 = GameState(pile1)
    game1.make_move(0, 1)
    assert game1 == GameState([0, 5, 3])


def test_get_legal_moves():
    game = GameState([0, 1, 3])
    assert get_legal_moves(game) is [(1, 1), (2, 1), (2, 2), (2, 3)]


def main():
    test_eq()
    test_is_legal_move()
    test_make_move()

    print("All tests pass")


if __name__ == "__main__":
    main()
