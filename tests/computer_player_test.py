import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../src"))
from game import Game
from computer_player import ComputerPlayer


class ComputerPlayerTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.computer_player = ComputerPlayer()

    def test_get_first_available_move(self):
        # Center tile preferred
        assert ComputerPlayer._get_first_available_move(self.game) == (1, 1)

        # 0, 1
        self.game.state = [
            ['x', 'o', 'x'],
            ['', 'o', 'o'],
            ['x', '', '']
        ]
        assert ComputerPlayer._get_first_available_move(self.game) == (0, 1)

    def test_no_first_available_move(self):
        # No space left
        self.game.state = [
            ['x', 'o', 'x'],
            ['o', 'x', 'o'],
            ['x', 'o', 'x']
        ]
        assert ComputerPlayer._get_first_available_move(self.game) == (None, None)

    def test_get_blocking_move_in_row(self):
        # No blocking move
        assert self.computer_player._get_blocking_move(self.game) == (None, None)

        # X in 1,0 blocks O
        self.game.state = [
            ['o', '', 'o'],
            ['x', '', 'x'],
            ['', '', '']
        ]
        assert self.computer_player._get_blocking_move(self.game) == (1, 0)

    def test_get_blocking_move_in_column(self):
        # No blocking move
        assert self.computer_player._get_blocking_move(self.game) == (None, None)

        # X in 0,2 blocks O
        self.game.state = [
            ['o', '', 'x'],
            ['o', '', 'x'],
            ['', '', '']
        ]
        assert self.computer_player._get_blocking_move(self.game) == (0, 2)

    def test_get_blocking_move_in_diagonal(self):
        # No blocking move
        assert self.computer_player._get_blocking_move(self.game) == (None, None)

        # X in 2,2 blocks O
        self.game.state = [
            ['o', 'x', 'x'],
            ['', 'o', ''],
            ['', '', '']
        ]
        assert self.computer_player._get_blocking_move(self.game) == (2, 2)

    def test_get_no_blocking_move_available(self):
        # No space left
        self.game.state = [
            ['x', 'o', 'x'],
            ['o', 'x', 'o'],
            ['x', 'o', 'x']
        ]
        assert self.computer_player._get_blocking_move(self.game) == (None, None)

    def test_get_winning_move_in_row(self):
        # No blocking move
        assert self.computer_player._get_winning_move(self.game) == (None, None)

        # X in 1,1 wins
        self.game.state = [
            ['o', '', 'o'],
            ['x', '', 'x'],
            ['', '', '']
        ]
        assert self.computer_player._get_winning_move(self.game) == (1, 1)

    def test_get_winning_move_in_column(self):
        # No blocking move
        assert self.computer_player._get_blocking_move(self.game) == (None, None)

        # X in 0,2 wins
        self.game.state = [
            ['x', '', 'o'],
            ['x', '', 'o'],
            ['', '', '']
        ]
        assert self.computer_player._get_winning_move(self.game) == (0, 2)

    def test_get_winning_move_in_diagonal(self):
        # No blocking move
        assert self.computer_player._get_blocking_move(self.game) == (None, None)

        # X in 0,2 wins
        self.game.state = [
            ['o', 'o', 'x'],
            ['', 'x', ''],
            ['', '', '']
        ]
        assert self.computer_player._get_winning_move(self.game) == (0, 2)

    def test_get_no_winning_move_available(self):
        # No space left
        self.game.state = [
            ['x', 'o', 'x'],
            ['o', 'x', 'o'],
            ['x', 'o', 'x']
        ]
        assert self.computer_player._get_blocking_move(self.game) == (None, None)
