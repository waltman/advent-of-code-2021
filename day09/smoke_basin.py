import sys
import numpy as np

# read in the grid
with open(sys.argv[1]) as f:
    tmp = [[int(c) for c in line.rstrip()] for line in f]
rows = len(tmp)
cols = len(tmp[0])
grid = np.ones([rows+2, cols+2], int) * 10
grid[1:rows+1,1:cols+1] = tmp

# find low points
risk = 0
for row in range(1, grid.shape[0]-1):
    for col in range(1, grid.shape[1]-1):
        val = grid[row,col]
        if val < grid[row-1,col] and \
           val < grid[row+1,col] and \
           val < grid[row,col-1] and \
           val < grid[row,col+1]:
           risk += val+1
print('Part 1:', risk)

        
