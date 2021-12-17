import sys
import re

# parse input
with open(sys.argv[1]) as f:
    m = re.search(r'x=([\d\-]+)\.\.([\d\-]+), y=([\d\-]+)\.\.([\d\-]+)', f.readline())
    x1 = int(m.group(1))
    x2 = int(m.group(2))
    y1 = int(m.group(3))
    y2 = int(m.group(4))

best_ymax = -1e300
for vi in range(1000):
    v = vi
    y = 0
    ymax = 0
    while True:
        y += v
        ymax = max(ymax, y)
        if y1 <= y <= y2:
            print(f'Hit! {vi=} {ymax=}')
            best_ymax = max(best_ymax, ymax)
            break
        elif y < y1:
            break
        else:
            v -= 1
print('Part 1:', best_ymax)
