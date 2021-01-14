import numpy as np
from unittest import TestCase

import xo


class AppTestSuits(TestCase):
    def test_create_board(self):
        xo.create_board()

    def test_player_1_win_column(self):
        board = xo.create_board()

        xo.place(board, 1, (0,0))
        xo.place(board, 1, (1,0))
        xo.place(board, 1, (2,0))

        self.assertEqual(xo.evaluate(board), 1)

    def test_player_2_win_row(self):
        board = xo.create_board()

        board[(0,0)] = 2
        board[(0,1)] = 2
        board[(0,2)] = 2

        self.assertEqual(xo.evaluate(board), 2)

    def test_player_1_win_diag_1(self):
        board = xo.create_board()

        board[(0,0)] = 1
        board[(1,1)] = 1
        board[(2,2)] = 1

        self.assertEqual(xo.evaluate(board), 1)

    def test_player_1_win_diag_2(self):
        board = xo.create_board()

        board[(2,0)] = 1
        board[(1,1)] = 1
        board[(0,2)] = 1

        self.assertEqual(xo.evaluate(board), 1)

    def test_ongoing(self):
        board = np.array([
            [1, 2, 1],
            [1, 1, 2],
            [2, 1, 2]
	])

        self.assertEqual(xo.evaluate(board), -1)
