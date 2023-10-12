import os
import sys
import unittest

import pytest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../src"))
from game import Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_get_all_possible_lines(self):
        self.game.state = [
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

        output = self.game._get_all_possible_lines()

        assert output == expected

    def test_get_winner(self):
        # No winner & game in progress
        assert self.game._get_winner() is None

        # No winner & draw
        self.game.state = [
            ["x", "o", "x"],
            ["x", "o", "x"],
            ["o", "x", "o"]
        ]
        assert self.game._get_winner() == 'x'

        # X wins horizontally
        self.game.state = [
            ["x", "x", "x"],
            ["o", "o", ""],
            ["o", "", ""]
        ]
        assert self.game._get_winner() == 'x'

        # x wins vertically
        self.game.state = [
            ["x", "x", "o"],
            ["o", "x", ""],
            ["o", "x", ""]
        ]
        assert self.game._get_winner() == 'x'

        # o wins diagonally
        self.game.state = [
            ["x", "x", "o"],
            ["x", "o", ""],
            ["o", "", ""]
        ]
        assert self.game._get_winner() == 'o'

    def test_submit_play(self):
        assert self.game.state[0][0] == ""

        # X plays a valid move
        self.game.submit_play('x', 0, 0)
        assert self.game.state[0][0] == 'x'
        assert self.game.next_player == 'o'

        # O plays a valid move
        self.game.submit_play('o', 1, 1)
        assert self.game.state[1][1] == 'o'
        assert self.game.next_player == 'x'

        # O tries to play again...
        with pytest.raises(Exception) as e_info:
            self.game.submit_play('o', 1, 0)
        assert self.game.state[0][1] == ""
        assert self.game.next_player == 'x'
        assert e_info.value.args[0] == "It is not o's turn, x is next!"

        # X tries to take O's placed tile...
        with pytest.raises(Exception) as e_info:
            self.game.submit_play('x', 1, 1)
        assert self.game.state[1][1] == "o"
        assert self.game.next_player == 'x'
        assert e_info.value.args[0] == "1,1 is not empty, contains: 'o'!"

        # Y plays a move...
        with pytest.raises(Exception) as e_info:
            self.game.submit_play('y', 2, 2)
        assert self.game.state[2][2] == ""
        assert self.game.next_player == 'x'
        assert e_info.value.args[0] == "y is not a valid play, must be 'x' or 'o'"
