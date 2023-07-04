import os
import sys
import unittest

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

        assert len(output) == 8
        for i in range(0, 8):
            assert output[i] == expected[i]

    def test_get_winner(self):
        pass

    def test_submit_play(self):
        pass
