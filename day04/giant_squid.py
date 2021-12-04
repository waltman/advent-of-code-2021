import sys
import numpy as np

def is_winner(mat):
    for row in range(5):
        if not np.any(mat[row][:]):
            return True
    for col in range(5):
        if not np.any(mat[:][col]):
            return True
    return False

# parse the input
boards = []
marks = []
with open(sys.argv[1]) as f:
    numbers = [int(n) for n in f.readline().split(',')]
    board = []
    for line in f:
        line = line.rstrip()
        if line == '':
            continue
        board.append([int(n) for n in line.split()])
        if len(board) == 5:
            boards.append(np.array(board))
            marks.append(np.array([[True for _ in range(5)] for _ in range(5)]))
            board = []

done = False
for number in numbers:
    if done:
        break
    for i in range(len(boards)):
        marks[i][np.where(boards[i] == number)] = False
        if is_winner(marks[i]):
            print('Part 1:', sum(boards[i][np.where(marks[i])]) * number)
            done = True
            break
