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

rules2 = [(action, x1-minx, x2-minx+1, y1-miny, y2-miny+1, z1, z2) for (action, x1, x2, y1, y2, z1, z2) in rules]
cnt = 0
cache = dict()
RES = 2758514936282235
#for z in range(minz, maxz+1):
for z in range(8913, maxz+1):
    # check with rules apply
    valid_rules = []
    for i in range(len(rules2)):
        (action, x1, x2, y1, y2, z1, z2) = rules2[i]
        if z1 <= z <= z2:
            valid_rules.append(i)
    valid_rules = tuple(valid_rules)

    # have we already solved this one?
    if valid_rules in cache:
        cnt += cache[valid_rules]
    else:
        mat = np.zeros([maxx-minx+1,maxy-miny+1], bool)
        num_ons = 0
        num_offs = 0
        onsize = 0
        for i in valid_rules:
            (action, x1, x2, y1, y2, z1, z2) = rules2[i]
            print(action, x1, x2, y1, y2, z1, z2)
            if action == 'on':
                mat[x1:x2, y1:y2] = True
                onsize = (x2-x1) * (y2-y1)
                num_ons += 1
            else:
                mat[x1:x2, y1:y2] = False
                num_offs += 1
        if num_ons == 1 and num_offs == 0:
            cache[valid_rules] = onsize
            cnt += cache[valid_rules]
        elif num_ons > 0:
            cache[valid_rules] = np.count_nonzero(mat)
            cnt += cache[valid_rules]

    print(z, cnt, onsize, num_ons, num_offs, RES-cnt)

print('Part 2:', cnt)
