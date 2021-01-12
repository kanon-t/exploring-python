#exercise 1
import numpy as np
def create_board():
    return np.zeros((3,3), dtype = int)


#exercise 2
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    
board = create_board()
place(board, 1, (0,0))


#exercise 3
def possibilities(board):
    x, y = np.where(board == 0)
    return [(x[i], y[i]) for i in range(len(x))]

possibilities(board)


#exercise 4
import random 
random.seed(1)

# write your code here!
def random_place(board, player):
    selection = possibilities(board)
    if selection:
        position = random.choice(selection)
        place(board, player, position)
    return board

random_place(board, 2)


#exercise 5
random.seed(1)
board = create_board()

# write your code here!
for i in range(3):
    for player in [1,2]:
        random_place(board, player)
        
print(board)


#exercise 6
def row_win(board, player):
    return np.any(np.all(board==player, axis=1))


row_win(board, 1)

#exercise 7
def col_win(board, player):
    return np.any(np.all(board==player, axis=0))

#testing
grid1 = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])
assert col_win(grid1, 1) == False

grid2 = np.array([
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]
])
assert col_win(grid2, 1) == True

grid3 = np.array([
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 0]
])
assert col_win(grid3, 1) == False

grid4 = np.array([
    [1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]
])
assert col_win(grid4, 1) == False

grid5 = np.array([
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
])
assert col_win(grid5, 1) == True

col_win(board, 1)

board[1,1] = 2


#exercise 8
def diag_win(board, player):
    return np.all(np.diag(board==player)) or \
        np.all(np.diag(np.fliplr(board) == player))

#testing
grid6 = np.array([
    [1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]
])
assert diag_win(grid6, 1) == False

grid7 = np.array([
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
])
assert diag_win(grid7, 1) == False

grid8 = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
assert diag_win(grid8, 1) == True

grid9 = np.array([
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
])
assert diag_win(grid9, 1) == True

diag_win(board, 2)


#exercise 9
def evaluate(board):
    for player in [1, 2]:
        for function in [row_win, col_win, diag_win]:
            if function(board, player):
                return player
    return 0 if possibilities(board) else -1

#testing
grid10 = np.array([
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
])

assert evaluate(grid10) == 1

grid11 = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0]
])

assert evaluate(grid11) == 0

grid12 = np.array([
    [0, 0, 2],
    [0, 1, 2],
    [1, 0, 2]
])

assert evaluate(grid12) == 2

grid13 = np.array([
    [2, 1, 2],
    [1, 2, 1],
    [1, 2, 1]
])

assert evaluate(grid13) == -1

evaluate(board)


#exercise 10
random.seed(1)

def play_game():
    board = create_board()
    winner = 0
    while True:
        for player in [1,2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                return winner

results = [play_game() for i in range(1000)]

from collections import Counter
Counter(results)
#or results.count(1)


#exercise 11
random.seed(1)

def play_strategic_game():
    board = create_board()
    board[1,1] = 1
    while True:
        for player in [2,1]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                return winner

wins = [play_strategic_game() for i in range(1000)]

from collections import Counter
Counter(wins)
