"""
This file handles the GameState class
"""


class GameState:
    def __init__(self, piles: list[int]):
        """
        piles is a list of integers where each integer represents a
        pile size in the game of Nim
        """
        self.piles = piles

    def __str__(self) -> str:
        s = ""
        for i, pile in enumerate(self.piles):
            s += f"Pile {i+1}:\t{pile}\n"
        return s

    def __eq__(self, other: 'GameState') -> bool:
        if not isinstance(other, GameState):
            return False
        if len(self.piles) != len(other.piles):
            return False
        return all(x == y for x, y in zip(self.piles, other.piles))

    def is_empty(self) -> bool:
        '''
        Returns True if and only if there are no stones in any pile
        '''
        for pile in self.piles:
            if pile != 0:
                return False
        return True

    def is_legal_move(self, m: int, n: int) -> bool:
        """
        Returns True if and only if (m, n) is a legal move
        where m is the pile index and n is the number of stones.
        Used in the construction of make_move
        """
        if 0 <= m < len(self.piles):
            if 1 <= n <= self.piles[m]:
                return True
        return False

    def make_move(self, m: int, n: int) -> bool:
        """
        If allowed, this will remove n stones from the pile in index m.
        If the move is illegal this will return False and do nothing.
        If the move is legal it will update self's piles and return True
        """
        if not self.is_legal_move(m, n):
            return False
        self.piles[m] -= n
        return True
