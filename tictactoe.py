from typing import List

def play():
    pass


def get_all_possible_lines(rows: List[List[str]]):
    """
    For the given game state, represented by a list o
    :param game_board:
    :return:
    """
    all_possible_lines: List[List[str]] = [][]

    # Get all rows
    for row in rows:
        all_possible_lines.append(row.copy())


    # Add all columns


    # Add all diagonals


    assert len(all_possible_lines) == 8
    return all_possible_lines


if __name__ == '__main__':
    play()
