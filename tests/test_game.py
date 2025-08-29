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

        self.assertEqual(output, expected)

    def test_get_winner(self):
        # No winner & game in progress
        self.game.state = [
            ["x", "o", "x"],
            ["", "", ""],
            ["", "", ""]
        ]
        assert self.game._get_winner() is None

        # No winner & draw
        self.game.state = [
            ["x", "o", "x"],
            ["x", "o", "x"],
            ["o", "x", "o"]
        ]
        self.assertEqual(self.game._get_winner(), 'draw')

        # X wins horizontally
        self.game.state = [
            ["x", "x", "x"],
            ["o", "o", ""],
            ["o", "", ""]
        ]
        self.assertEqual(self.game._get_winner(), 'x')

        # x wins vertically
        self.game.state = [
            ["x", "x", "o"],
            ["o", "x", ""],
            ["o", "x", ""]
        ]
        self.assertEqual(self.game._get_winner(), 'x')

        # o wins diagonally
        self.game.state = [
            ["x", "x", "o"],
            ["x", "o", ""],
            ["o", "", ""]
        ]
        self.assertEqual(self.game._get_winner(), 'o')

    def test_submit_play(self):
        self.assertEqual(self.game.state[0][0], "")

        # X plays a valid move
        self.game.submit_play('x', 0, 0)
        self.assertEqual(self.game.state[0][0], 'x')
        self.assertEqual(self.game.next_player, 'o')

        # O plays a valid move
        self.game.submit_play('o', 1, 1)
        self.assertEqual(self.game.state[1][1], 'o')
        self.assertEqual(self.game.next_player, 'x')

        # O tries to play again...
        with self.assertRaises(Exception) as cm:
            self.game.submit_play('o', 1, 0)
        self.assertEqual(self.game.state[0][1], "")
        self.assertEqual(self.game.next_player, 'x')
        self.assertEqual(str(cm.exception), "It is not o's turn, x is next!")

        # X tries to take O's placed tile...
        with self.assertRaises(Exception) as cm:
            self.game.submit_play('x', 1, 1)
        self.assertEqual(self.game.state[1][1], "o")
        self.assertEqual(self.game.next_player, 'x')
        self.assertEqual(str(cm.exception), "1,1 is not empty, contains: 'o'!")

        # Y plays a move...
        with self.assertRaises(Exception) as cm:
            self.game.submit_play('y', 2, 2)
        self.assertEqual(self.game.state[2][2], "")
        self.assertEqual(self.game.next_player, 'x')
        self.assertEqual(str(cm.exception), "y is not a valid play, must be 'x' or 'o'")


if __name__ == "__main__":
    unittest.main()
