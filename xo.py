"""Module for naughts-and-crosses game."""
import random

import numpy as np


#exercise 1
def create_board():
    """Creates a 3x3 naughts-and-crosses board."""
    return  np.zeros((3,3), dtype = int)


#exercise 2
def place(board, player, position):
    """Places player in empty grid."""
    if board[position] == 0:
        board[position] = player


#exercise 3
def possibilities(board):
    """Finds all empty board spaces."""
    x_coord, y_coord = np.where(board == 0)
    return [(x_coord[i], y_coord[i]) for i in range(len(x_coord))]


#exercise 4
def random_place(board, player):
    """Checks for empty space on board and returns board with player placed at random location."""
    selection = possibilities(board)
    if selection:
        position = random.choice(selection)
        place(board, player, position)
    return board


#exercise 6
def row_win(board, player):
    """Assesses congruency of player across row."""
    return np.any(np.all(board==player, axis=1))


#exercise 7
def col_win(board, player):
    """Assesses congruency of player across column."""
    return np.any(np.all(board==player, axis=0))


#exercise 8
def diag_win(board, player):
    """Assesses diagonal congruency of player."""
    return np.all(np.diag(board==player)) or \
        np.all(np.diag(np.fliplr(board) == player))


#exercise 9
def evaluate(board):
    """Checks for any wins and returns player number; otherwise, returns -1 for a draw."""
    for player in [1, 2]:
        for function in [row_win, col_win, diag_win]:
            if function(board, player):
                return player
    return 0 if possibilities(board) else -1


#exercise 11
def play_strategic_game():
    """Plays randomised game but with player 1 always starting in the middle, and returns winner."""
    board = create_board()
    board[1,1] = 1
    while True:
        for player in [2,1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                return winner
