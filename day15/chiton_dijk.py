import sys
import networkx as nx
from heapq import heappush, heappop

def neighbors(row, col, num_rows, num_cols):
    neighs = [(row-1,col),
              (row+1,col),
              (row,col-1),
              (row,col+1)]
    for r,c in neighs:
        if 0 <= r < num_rows and 0 <= c < num_cols:
            yield r,c

def dijk(grid, num_rows, num_cols):
    h = [(0, (0,0))]
    dst = {}
    visited = set()
    while h:
        d, p = heappop(h)
        row,col = p
        if (row,col) not in visited:
            visited.add((row,col))
            if row == num_rows-1 and col == num_cols-1:
                return dst[(row,col)]
            else:
                for r,c in neighbors(row, col, num_rows, num_cols):
                    if (r,c) not in visited:
                        dst[(r,c)] = min(dst.get((r,c), float('inf')), d + grid[r][c])
                        heappush(h, (dst[(r,c)], (r,c)))

# parse the input
with open(sys.argv[1]) as f:
    grid = [[int(c) for c in line.rstrip()] for line in f]
num_rows = len(grid)
num_cols = len(grid[0])

print('Part 1 (dijk):', dijk(grid, num_rows, num_cols))

# expand first num_rows rows
for row in range(num_rows):
    for col in range(num_cols, num_cols*5):
        grid[row].append(1 if (val := grid[row][col-num_cols]) == 9 else val+1)

# add the remaining rows
for row in range(num_rows, num_rows*5):
    grid.append([1 if (val := grid[row-num_rows][col]) == 9 else val+1 for col in range(num_cols*5)])

print('Part 2 (dijk):', dijk(grid, num_rows*5, num_cols*5))
