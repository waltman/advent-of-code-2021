import sys
import numpy as np

def pixel_val(grid, row, col):
    return int(''.join([str(i) for i in grid[row-1:row+2,col-1:col+2].flatten()]), 2)

# parse the input
with open(sys.argv[1]) as f:
    alg = [0 if c == '.' else 1 for c in f.readline().rstrip()]
    f.readline()
    lines = np.array([[0 if c == '.' else 1 for c in line.rstrip()] for line in f], int)
    
# put it in a grid with some buffer
BUFFER = 120
B2 = BUFFER//2
grid = np.zeros((lines.shape[0]+BUFFER, lines.shape[1]+BUFFER), int)
grid[B2:B2+lines.shape[0],B2:B2+lines.shape[1]] = lines

for step in range(50):
    if step % 2 == 0:
        new_grid = np.ones(grid.shape, int)
    else:
        new_grid = np.zeros(grid.shape, int)
    # new_grid = np.zeros(grid.shape, int)
    for row in range(1,grid.shape[0]-1):
        for col in range(1,grid.shape[1]-1):
            new_grid[row,col] = alg[pixel_val(grid, row, col)]
    grid = new_grid
    if step == 1:
        print('Part 1:', sum(grid.flatten()))

print('Part 2:', sum(grid.flatten()))
