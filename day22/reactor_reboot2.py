import sys
import re
import numpy as np

rules = []
(minx, miny, minz, maxx, maxy, maxz) = (float('inf'), float('inf'), float('inf'), float('-inf'), float('-inf'), float('-inf'))
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

        minx = min(x1, minx)
        miny = min(y1, miny)
        minz = min(z1, minz)
        maxx = max(x1, maxx)
        maxy = max(y1, maxy)
        maxz = max(z1, maxz)

        rules.append((action, x1, x2, y1, y2, z1, z2))

cnt = 0
for z in range(minz, maxz+1):
    mat = np.zeros([maxx-minx+1,maxy-miny+1], bool)
    for (action, x1, x2, y1, y2, z1, z2) in rules:
        if z1 <= z <= z2:
            if action == 'on':
                mat[x1+minx:x2+minx+1,y1+miny:y2+miny+1] = 1
            else:
                mat[x1+minx:x2+minx+1,y1+miny:y2+miny+1] = 0
    cnt += np.count_nonzero(mat)
    print(z, cnt)

print('Part 2:', cnt)
