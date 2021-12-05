import sys
import numpy as np
import re

def diag_points(x1,y1,x2,y2):
    dx = 1 if x1 < x2 else -1
    dy = 1 if y1 < y2 else -1
    cnt = abs(x1-x2) + 1
    x,y = x1,y1
    for _ in range(cnt):
        yield(x,y)
        x += dx
        y += dy

# parse the input
lines = []
with open(sys.argv[1]) as f:
    for line in f:
        t1, t2 = re.split(' -> ', line.rstrip())
        x1,y1 = [int(x) for x in t1.split(',')]
        x2,y2 = [int(x) for x in t2.split(',')]
        lines.append((x1,y1,x2,y2))

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
        for x,y in diag_points(x1,y1,x2,y2):
            grid[y,x] += 1
print('Part 2:', len(grid[np.where(grid > 1)]))
