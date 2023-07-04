import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../src"))
from game import Game
from computer_player import ComputerPlayer


class ComputerPlayerTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.computer_player = ComputerPlayer('x')

    def test_get_first_available_move(self):
        # Top left
        assert ComputerPlayer._get_first_available_move(self.game) == (0, 0)

        # 0, 1
        self.game.state = [
            ['x', 'o', 'x'],
            ['', '', 'o'],
            ['x', '', '']
        ]
        assert ComputerPlayer._get_first_available_move(self.game) == (0, 1)

        # No space left
        self.game.state = [
            ['x', 'o', 'x'],
            ['o', 'x', 'o'],
            ['x', 'o', 'x']
        ]
        assert ComputerPlayer._get_first_available_move(self.game) == (None, None)

    def test_get_blocking_move(self):
        # No blocking move
        assert self.computer_player._get_blocking_move(self.game) == (None, None)

        # X in 1, 0 blocks O
        self.game.state = [
            ['o', '', 'o'],
            ['x', '', 'x'],
            ['', '', '']
        ]
        assert self.computer_player._get_blocking_move(self.game) == (1, 0)

        # No space left
        self.game.state = [
            ['x', 'o', 'x'],
            ['o', 'x', 'o'],
            ['x', 'o', 'x']
        ]
        assert self.computer_player._get_blocking_move(self.game) == (None, None)
