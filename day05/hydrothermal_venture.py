import sys
import numpy as np
import re

def diag_points(x1,y1,x2,y2):
    dx = 1 if x1 < x2 else -1
    dy = 1 if y1 < y2 else -1
    x = range(x1, x2+dx, dx)
    y = range(y1, y2+dy, dy)
    return y,x

# parse the input
lines = []
with open(sys.argv[1]) as f:
    for line in f:
        m = re.search('(\d+),(\d+) -> (\d+),(\d+)', line)
        lines.append([int(x) for x in m.group(1,2,3,4)])

grid = np.zeros([1000,1000],int)
for x1,y1,x2,y2 in lines:
    if x1 == x2:
        yfrom, yto = sorted([y1,y2])
        grid[yfrom:yto+1,x1] += 1
    elif y1 == y2:
        xfrom, xto = sorted([x1,x2])
        grid[y1,xfrom:xto+1] += 1
print('Part 1:', len(grid[np.where(grid > 1)]))

for x1,y1,x2,y2 in lines:
    if x1 != x2 and y1 != y2:
        grid[diag_points(x1,y1,x2,y2)] += 1
print('Part 2:', len(grid[np.where(grid > 1)]))
