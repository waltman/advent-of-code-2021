import sys
from Monad import Monad
from itertools import product
from random import randint

with open(sys.argv[1]) as f:
    pgm = [line.rstrip() for line in f]

step = 0
best = -1

# while True:
#     step += 1
#     if step % 100_000 == 0:
#         print(f'{step=}, {pr=}, {best=}')
#     pr = [randint(1,9) for _ in range(14)]
#     monad = Monad(pgm, pr)
#     monad.run()
#     if monad.reg['z'] == 0:
#         print(pr, monad.reg['z'])
#         best = ''.join(pr)

#for pr in product(range(1,10), repeat=14):
for pr in product(range(9,0,-1), repeat=1):
    step += 1
    if step % 100_000 == 0:
        print(f'{step=}, {pr=}, {best=}')
    
    monad = Monad(pgm, pr)
    monad.run()
    print(pr, monad.reg)
    if monad.reg['z'] == 0:
        print(pr, monad.reg['z'])
        best = ''.join(pr)
