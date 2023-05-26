from typing import List

def play():
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
    all_possible_lines: List[List[str]] = [][]

    # Get all rows
    for row in rows:
        all_possible_lines.append(row.copy())

    # TODO - Add all columns


    # TODO - Add all diagonals


    assert len(all_possible_lines) == 8
    return all_possible_lines


if __name__ == '__main__':
    play()
