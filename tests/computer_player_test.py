import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../src"))
from game import Game
from computer_player import ComputerPlayer


class ComputerPlayerTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_get_first_available_move(self):
        # Top left
        assert ComputerPlayer._get_first_available_move(self.game) == (0, 0)

        # 0, 1
        self.game.state = [
            ['x', 'o', 'x'],
            ['', '', 'o'],
            ['x', '', ''],
        ]
        assert ComputerPlayer._get_first_available_move(self.game) == (0, 1)

        # None
        self.game.state = [
            ['x', 'o', 'x'],
            ['o', 'x', 'o'],
            ['x', 'o', 'x'],
        ]
        assert ComputerPlayer._get_first_available_move(self.game) == (None, None)
