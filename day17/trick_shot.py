import sys
import re

def hit_target(x1,x2,y1,y2,vix,viy):
    x = 0
    vx = vix
    y = 0
    vy = viy
    while True:
        x += vx
        vx = max(0, vx-1)
        y += vy
        vy -= 1
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True
        elif x > x2 or y < y1:
            return False

# parse input
with open(sys.argv[1]) as f:
    m = re.search(r'x=([\d\-]+)\.\.([\d\-]+), y=([\d\-]+)\.\.([\d\-]+)', f.readline())
    x1 = int(m.group(1))
    x2 = int(m.group(2))
    y1 = int(m.group(3))
    y2 = int(m.group(4))

# part 1
best_ymax = -1e300
for vy in range(1000):
    v = vy
    y = 0
    ymax = 0
    while True:
        y += v
        ymax = max(ymax, y)
        if y1 <= y <= y2:
            best_ymax = max(best_ymax, ymax)
            break
        elif y < y1:
            break
        else:
            v -= 1
print('Part 1:', best_ymax)

# part 2
cnt = 0
for vix in range(x2+1):
    for viy in range(y1,500):
        if hit_target(x1,x2,y1,y2,vix,viy):
            cnt += 1
print('Part 2:', cnt)
