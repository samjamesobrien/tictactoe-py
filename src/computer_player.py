import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__))))
from game import Game


class ComputerPlayer:

    @staticmethod
    def play(game: Game):
        """
        For the given Game, choose a next move for the player and play it.
        :param game: the game in progress.
        """

        # Try to block
        x, y = ComputerPlayer._get_blocking_move(game)
        if x and y:
            game.submit_play(game.next_player, x, y)

        # try to win
        x, y = ComputerPlayer._get_winning_move(game)
        if x and y:
            game.submit_play(game.next_player, x, y)

        # take any move
        x, y = ComputerPlayer._get_first_available_move(game)
        if x and y:
            game.submit_play(game.next_player, x, y)

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
        :return: x & y coordinates that represent a blocking move, else None, None
        """
        next_player = game.next_player

        # TODO - is there a move where we can block the other player?

        return None, None

    def _get_winning_move(self, game: Game):
        """
        Return a move that wins the game.
        :return: x & y coordinates that represent a winning move, else None, None
        """
        next_player = game.next_player

        # TODO - is there a move where we can win?

        return None, None
