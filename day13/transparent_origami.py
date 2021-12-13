import sys
import numpy as np
import re

#grid = np.zeros([15,11], bool)
grid = np.zeros([894,1311], bool)
with open(sys.argv[1]) as f:
    # read in points
    for line in f:
        line = line.rstrip()
        if line == '':
            break
        col, row = map(int, line.split(','))
#        print(col, row)
        grid[row,col] = True
#    print(grid.astype(int))

    # handle folds
    fold = 1
    for line in f:
        m = re.match('fold along (.)=(\d+)', line)
        axis = m.group(1)
        val = int(m.group(2))
#        print(axis, val)
        if axis == 'x':
#            print(grid[:,0:val].astype(int))
#            print(np.fliplr(grid[:,val+1:].astype(int)))
            tmp = grid[:,0:val] | np.fliplr(grid[:,val+1:])
        else:
#            print(grid[0:val,:].astype(int))
#            print(np.flipud(grid[val+1:,:].astype(int)))
            tmp = grid[0:val,:] | np.flipud(grid[val+1:,:])
#        print(tmp.astype(int))
        grid = tmp
        print(sum(sum(grid)))
        if fold == 1:
            print('Part 1:', sum(sum(grid)))
        fold += 1
