import sys
import os
from typing import Optional

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__))))
from game import Game


class ComputerPlayer:
    """
    A Player who makes a play on the game.
    """

    def __init__(self, my_letter: str):
        self.my_letter = my_letter

    def play(self, game: Game):
        # Try to block
        x, y = self._get_blocking_move(game)
        if x and y:
            game.submit_play(self.my_letter, x, y)

        # try to win
        x, y = self._get_winning_move(game)
        if x and y:
            game.submit_play(self.my_letter, x, y)

        # take any move
        x, y = self._get_first_available_move(game)
        if x and y:
            game.submit_play(self.my_letter, x, y)

    @staticmethod
    def _get_first_available_move(game: Game):
        """
        Return any move available to the player in the format X, Y
        """
        for x in range(0, 2):
            for y in range(0, 2):
                if game.state[y][x] == "":
                    return x, y
        return None, None

    def _get_blocking_move(self, game: Game):
        """
        Return a move that blocks the other player from winning.
        """
        # TODO - is there a move where we can block the other player?

        return None, None

    def _get_winning_move(self, game: Game):
        """
        Return a move that wins the game.
        """
        # TODO - is there a move where we can win?

        return None, None
