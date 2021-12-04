import sys
import numpy as np

def is_winner(mat):
    for row in range(5):
        if not np.any(mat[row,:]):
            return True
    for col in range(5):
        if not np.any(mat[:,col]):
            return True
    return False

# parse the input
boards = []
unmarked = []
with open(sys.argv[1]) as f:
    numbers = map(int, f.readline().split(','))
    board = []
    for line in f:
        line = line.rstrip()
        if line == '':
            continue
        board.append([int(n) for n in line.split()])
        if len(board) == 5:
            boards.append(np.array(board))
            unmarked.append(np.array([[True for _ in range(5)] for _ in range(5)]))
            board = []

alive = {*range(len(boards))}
for number in numbers:
    if not alive:
        break
    for i in list(alive):
        unmarked[i][np.where(boards[i] == number)] = False
        if is_winner(unmarked[i]):
            if len(alive) == len(boards):
                print('Part 1:', sum(boards[i][np.where(unmarked[i])]) * number)
            elif len(alive) == 1:
                print('Part 2:', sum(boards[i][np.where(unmarked[i])]) * number)
            alive.remove(i)
