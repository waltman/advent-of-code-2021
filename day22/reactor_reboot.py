import sys
import re
import numpy as np
from itertools import product

def scale_range(p1, p2):
    MAX = 50
    p1 = max(p1, -MAX)
    p2 = min(p2, MAX)
    return range(p1+MAX, p2+MAX+1)

grid = np.zeros([101,101,101], bool)
with open(sys.argv[1]) as f:
    for line in f:
        m = re.match(r'([^ ]+) x=([\-\d]+)\.\.([\-\d]+),y=([\-\d]+)\.\.([\-\d]+),z=([\-\d]+)\.\.([\-\d]+)', line.rstrip())
        action = m.group(1)
        x1 = int(m.group(2))
        x2 = int(m.group(3))
        y1 = int(m.group(4))
        y2 = int(m.group(5))
        z1 = int(m.group(6))
        z2 = int(m.group(7))

        r1 = scale_range(x1, x2)
        r2 = scale_range(y1, y2)
        r3 = scale_range(z1, z2)
        grid_range = np.array([x for x in product(r1,r2,r3)])
        if grid_range.shape[0] == 0:
            continue
        if action == 'on':
            grid[grid_range[:,0],grid_range[:,1],grid_range[:,2]] = True
        else:
            grid[grid_range[:,0],grid_range[:,1],grid_range[:,2]] = False

print('Part 1:', sum(grid.flatten()))

