import os
import sys
import unittest
import pytest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../src"))
from game import Game
from computer_player import ComputerPlayer


class ComputerPlayerTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_play
