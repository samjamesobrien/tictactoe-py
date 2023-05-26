from typing import List

new_game = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

def submit_play(player: str, x: int, y: int):
    """
    Add a play to the game in progress, the player's letter and the target on the board
    :param player: 'x' or 'o'
    :param x: index across
    :param y: index down
    :return: the current game state, a winner, a draw, or in progress
    """
    pass


def get_all_possible_lines(rows: List[List[str]]):
    """
    There are 8 possible lines in tic tac toe, 3 horizontal, 3 vertical & 2 diagonal. Any of those 8 may win a game.
    :param rows the rows that represent a game in progress. e.g.
    [
      ["x", "o", ""],
      ["x", "o", ""],
      ["", "", ""]
    ]
    :return all possible lines of strings through the game board.
    """
    all_possible_lines: List[List[str]] = []

    # Get all rows
    for row in rows:
        all_possible_lines.append(row.copy())

    # TODO - Add all columns


    # TODO - Add all diagonals


    return all_possible_lines


if __name__ == '__main__':
    pass
