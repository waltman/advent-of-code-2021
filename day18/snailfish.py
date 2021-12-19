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
    for line in f:
        pair = Pair(eval(line.rstrip()))
        reduce(pair)
#         print(line, end='')
#         print(pair)
#         print(pair.depth())
#         expl = pair.explodable()
#         print('Explode:', expl)
# #        print(expl.reg_left().left, expl.reg_right().right)
#         expl.explode()
#         print(pair)
        print()

