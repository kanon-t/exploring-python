"""Test suits for naughts-and-crosses game."""
from unittest import TestCase
import numpy as np

import xo


class AppTestSuits(TestCase):
    """This is a test suit class."""
    def test_create_board(self):
        """Tests the create_board function."""
        xo.create_board()

    def test_player_1_win_column(self):
        """Tests col_win function with player 1."""
        board = xo.create_board()

        xo.place(board, 1, (0,0))
        xo.place(board, 1, (1,0))
        xo.place(board, 1, (2,0))

        self.assertEqual(xo.evaluate(board), 1)

    def test_player_2_win_row(self):
        """Tests row_win function with player 2."""
        board = xo.create_board()

        board[(0,0)] = 2
        board[(0,1)] = 2
        board[(0,2)] = 2

        self.assertEqual(xo.evaluate(board), 2)

    def test_player_1_win_diag_1(self):
        """Tests diag_win function with player 1."""
        board = xo.create_board()

        board[(0,0)] = 1
        board[(1,1)] = 1
        board[(2,2)] = 1

        self.assertEqual(xo.evaluate(board), 1)

    def test_player_1_win_diag_2(self):
        """Tests reversed diag_win function with player 1."""
        board = xo.create_board()

        board[(2,0)] = 1
        board[(1,1)] = 1
        board[(0,2)] = 1

        self.assertEqual(xo.evaluate(board), 1)

    def test_ongoing(self):
        """Tests evaluate(board) function."""
        board = np.array([
            [1, 2, 1],
            [1, 1, 2],
            [2, 1, 2]
	])

        self.assertEqual(xo.evaluate(board), -1)
