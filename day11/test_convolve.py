import sys
import numpy as np
from queue import Queue
from scipy import ndimage

def reset_flashed(m):
    m[:] = True
    m[1:m.shape[0]-1,1:m.shape[1]-1] = False

def neighbors(row, col):
    return [(row-1,col-1), (row-1,col), (row-1,col+1),
            (row,  col-1),              (row,  col+1),
            (row+1,col-1), (row+1,col), (row+1,col+1),
            ]

KERNEL = np.ones((3, 3), int)
def step(a):
    a += 1
    f = g = a > 9
    while g.any():
        a += ndimage.convolve(g.astype(int), KERNEL, mode="constant")
        g = (a > 9) & ~f
        f |= g
    a[f] = 0
    return f.sum()

# read in the grid
with open(sys.argv[1]) as f:
    grid = np.array([[int(c) for c in line.rstrip()] for line in f])

print(grid)
s = step(grid)
print(s)
print(grid)

