import sys
import numpy as np
from queue import Queue
from math import prod

def basin_size(low, grid):
    seen = set()
    q = Queue()
    q.put(low)
    size = 0
    while not q.empty():
        row, col = q.get()
        if (row,col) in seen:
            continue
        size += 1
        seen.add((row,col))
        for r,c in [(row+1,col), (row-1,col), (row,col+1), (row,col-1)]:
            if grid[r,c] <= 8 and (r,c) not in seen:
                q.put((r,c))
    return size

# read in the grid
with open(sys.argv[1]) as f:
    tmp = [[int(c) for c in line.rstrip()] for line in f]
rows = len(tmp)
cols = len(tmp[0])
grid = np.ones([rows+2, cols+2], int) * 10
grid[1:rows+1,1:cols+1] = tmp

# find low points
risk = 0
lows = []
for row in range(1, grid.shape[0]-1):
    for col in range(1, grid.shape[1]-1):
        val = grid[row,col]
        if val < grid[row-1,col] and \
           val < grid[row+1,col] and \
           val < grid[row,col-1] and \
           val < grid[row,col+1]:
           risk += val+1
           lows.append((row, col))
print('Part 1:', risk)

# find the basins
basins = [basin_size(low, grid) for low in lows]
print('Part 2:', prod(sorted(basins)[-3:]))
