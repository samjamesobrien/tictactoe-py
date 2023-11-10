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
        self.next_player = 'x'

    def submit_play(self, current_player: str, x: int, y: int):
        """
        Add a play to the game in progress, the player's letter and the target on the board
        :param current_player: 'x' or 'o'
        :param x: index across horizontally
        :param y: index down vertically
        :return: the current game state, a winner, a draw, or in progress
        """
        if current_player not in ["x", "o"]:
            raise Exception(f"{current_player} is not a valid play, must be 'x' or 'o'")

        if current_player is not self.next_player:
            raise Exception(f"It is not {current_player}'s turn, {self.next_player} is next!")

        if self.state[y][x] != "":
            raise Exception(f"{x},{y} is not empty, contains: '{self.state[y][x]}'!")

        self.state[y][x] = current_player
        self.next_player = 'o' if current_player is 'x' else 'x'

        return self._get_winner()

    def _get_winner(self) -> Optional[str]:
        """
        Evaluate the game state and return a winner, if any.
        :return: 'x', 'y' or 'draw' if no possible plays remain, otherwise None.
        """
        all_possible_lines = self._get_all_possible_lines()

        #
        # TODO - Evaluate all lines & return a winner if present
        #

        #
        # TODO - If it is a draw, return 'draw'
        #

        return

    def _get_all_possible_lines(self) -> List[List[str]]:
        """
        There are 8 possible lines through the board, 3 horizontal, 3 vertical & 2 diagonal.
        Any of those 8 may win a game.
        :return all possible lists of strings through the game board.
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
