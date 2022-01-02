import sys
from copy import deepcopy

# read in grid
grid = []
with open(sys.argv[1]) as f:
    for line in f:
        row = []
        for c in line.rstrip():
            if c == 'v' or c == '>':
                row.append(c)
            else:
                row.append('.')
        grid.append(row)

num_rows = len(grid)
num_cols = len(grid[0])

step = 1
done = False
while not done:
    done = True
    # move east
    new_grid = deepcopy(grid)
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == '>' and grid[row][(col+1) % num_cols] == '.':
                new_grid[row][col] = '.'
                new_grid[row][(col+1) % num_cols] = '>'
                done = False

    grid = deepcopy(new_grid)

    # move south
    grid = deepcopy(new_grid)
    new_grid = deepcopy(grid)
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 'v' and grid[(row+1) % num_rows][col] == '.':
                new_grid[row][col] = '.'
                new_grid[(row+1) % num_rows][col] = 'v'
                done = False

    if done:
        break
    else:
        step += 1
        grid = deepcopy(new_grid)

print('Part 1:', step)

# for row in range(num_rows):
#     for col in range(num_cols):
#         print(grid[row][col], end='')
#     print()
