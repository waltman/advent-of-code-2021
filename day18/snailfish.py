import sys
from Pair import Pair

def reduce(pair):
    while True:
        if node := pair.explodable():
            node.explode()
        elif node := pair.splittable():
            node.split()
        else:
            break

with open(sys.argv[1]) as f:
    lines = [line.rstrip() for line in f]

pair = Pair(eval(lines[0]))
reduce(pair)
for i in range(1, len(lines)):
    pairstr = f'[{pair},{lines[i]}]'
    pair = Pair(eval(pairstr))
    reduce(pair)

print('Part 1:', pair.magnitude())

best_mag = -1
for i in range(len(lines)):
    l1 = lines[i]
    pair = Pair(eval(l1))
    reduce(pair)
    save_pair = str(pair)
    for j in range(len(lines)):
        if i == j:
            continue
        l2 = lines[j]
        pairstr = f'[{save_pair},{l2}]'
        pair = Pair(eval(pairstr))
        reduce(pair)
        mag = pair.magnitude()
        best_mag = max(best_mag, mag)
print('Part 2:', best_mag)
