from nim_game import GameState


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


def main():
    test_eq()
    test_is_legal_move()
    test_make_move()

    print("All tests pass")


if __name__ == "__main__":
    main()
