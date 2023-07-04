from typing import List, Optional


class Game:
    """
    A Game of tic-tac-toe in progress.
    """

    def __init__(self):
        self.state = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def submit_play(self, player: str, x: int, y: int):
        """
        Add a play to the game in progress, the player's letter and the target on the board
        :param player: 'x' or 'o'
        :param x: index across
        :param y: index down
        :return: the current game state, a winner, a draw, or in progress
        """
        if player not in ["x", "o"]:
            raise Exception(f"{player} is not a valid play, must be 'x' or 'o'")

        if self.state[y][x] != "":
            raise Exception(f"{x},{y} is not empty, contains: '{self.state[y][x]}'!")

        self.state[y][x] = player

        return self._get_winner()

    def _get_winner(self) -> Optional[str]:
        """
        Evaluate the game state and return a winner, if any.
        :return:
        """
        all_possible_lines = self._get_all_possible_lines()

        #
        # TODO - Evaluate game state & return a winner
        #

        return

    def _get_all_possible_lines(self) -> List[List[str]]:
        """
        There are 8 possible lines in tic tac toe, 3 horizontal, 3 vertical & 2 diagonal.
        Any of those 8 may win a game.
        :return all possible lines of strings through the game board.
        """
        all_possible_lines: List[List[str]] = []

        # Get all rows
        for row in self.state:
            all_possible_lines.append(row.copy())

        #
        # TODO - Add all columns
        #

        #
        # TODO - Add all diagonals
        #

        return all_possible_lines
