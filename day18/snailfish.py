import sys
from Pair import Pair

def reduce(pair):
    print(pair)
    while True:
        if node := pair.explodable():
            print('exploding')
            node.explode()
            print(pair)
        elif node := pair.splittable():
            print('splitting')
            node.split()
            print(pair)
        else:
            break

with open(sys.argv[1]) as f:
    lines = [line.rstrip() for line in f]

pair = Pair(eval(lines[0]))
print('pair 0:', pair)
reduce(pair)
print('reduced:', pair)
for i in range(1, len(lines)):
    pairstr = f'[{pair},{lines[i]}]'
    pair = Pair(eval(pairstr))
    print('pair', i, pair)
    reduce(pair)
    print('reduced:', pair)

print('Part 1:', pair.magnitude())

best_mag = -1
tests = 0
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
        tests += 1
print('Part 2:', best_mag)
print(tests)

# pair_str = lines[0]
# for s in lines[1:]:
# print('read:', pair_str)
# pair = Pair(eval(pair_str))
# print('eval:', pair)
# reduce(pair)
# print('reduce:', pair)

#     for line in f:
#         pair = Pair(eval(line.rstrip()))
#         reduce(pair)
# #         print(line, end='')
# #         print(pair)
# #         print(pair.depth())
# #         expl = pair.explodable()
# #         print('Explode:', expl)
# # #        print(expl.reg_left().left, expl.reg_right().right)
# #         expl.explode()
# #         print(pair)
#         print()

