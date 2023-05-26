import os, sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from tictactoe import *


class TicTacToeTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_all_possible_lines(self):
        input = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

        expected = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["1", "4", "7"],
            ["2", "5", "8"],
            ["3", "6", "9"],
            ["1", "5", "9"],
            ["7", "5", "3"],
        ]

        output = get_all_possible_lines(input)

        assert 8 == len(output)
        for i in range(0, 8):
            assert output[i] == expected[i]


if __name__ == '__main__':
    unittest.main()
