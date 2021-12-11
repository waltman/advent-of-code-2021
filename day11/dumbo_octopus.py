import sys
import numpy as np
from queue import Queue

def reset_flashed(m):
    m[:] = True
    m[1:m.shape[0]-1,1:m.shape[1]-1] = False

def neighbors(row, col):
    return [(row-1,col-1), (row-1,col), (row-1,col+1),
            (row,  col-1),              (row,  col+1),
            (row+1,col-1), (row+1,col), (row+1,col+1),
            ]

# read in the grid
with open(sys.argv[1]) as f:
    tmp = [[int(c) for c in line.rstrip()] for line in f]
rows = len(tmp)
cols = len(tmp[0])
grid = np.zeros([rows+2, cols+2], int)
grid[1:rows+1,1:cols+1] = tmp
flashed = np.zeros(grid.shape, bool)

flashes = 0
step = 1
while (True):
    # Step 1
    grid[1:grid.shape[0]-1, 1:grid.shape[1]-1] += 1
    q = Queue()
    rows, cols = np.where(grid > 9)
    queued = set()
    for coords in zip(rows, cols):
        q.put(coords)
        queued.add(coords)

    # Step 2
    reset_flashed(flashed)
    while not q.empty():
        row, col = q.get()
        flashed[row,col] = True
        flashes += 1
        for r,c in neighbors(row, col):
            if not flashed[r,c]:
                grid[r,c] += 1
                if grid[r,c] > 9 and (r,c) not in queued:
                    q.put((r,c))
                    queued.add((r,c))

    # Step 3
    grid[np.where(grid > 9)] = 0

    # Check if we're done
    if step == 100:
        print('Part 1:', flashes)
    if (np.all(grid == 0)):
        print('Part 2:', step)
        break
    else:
        step += 1



