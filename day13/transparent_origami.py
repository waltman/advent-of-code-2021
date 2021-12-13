import sys
import numpy as np
import re

def round_up_odd(arr):
    biggest = max(arr)+1
    return biggest if biggest % 2 else biggest+1

with open(sys.argv[1]) as f:
    # read in points
    rows = []
    cols = []
    for line in f:
        line = line.rstrip()
        if line == '':
            break
        col, row = map(int, line.split(','))
        rows.append(row)
        cols.append(col)
    grid = np.zeros([round_up_odd(rows), round_up_odd(cols)], bool)
    grid[rows,cols] = True

    # handle folds
    fold = 1
    for line in f:
        m = re.match('fold along (.)=(\d+)', line)
        axis = m.group(1)
        val = int(m.group(2))
        if axis == 'x':
            grid = grid[:,0:val] | np.fliplr(grid[:,val+1:])
        else:
            grid = grid[0:val,:] | np.flipud(grid[val+1:,:])
        print(sum(sum(grid)))
        if fold == 1:
            print('Part 1:', sum(sum(grid)))
        fold += 1

print('Part 2:')
for row in range(grid.shape[0]):
    for col in range(grid.shape[1]):
        print('#' if grid[row,col] else ' ', end='')
    print()
