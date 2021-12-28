import sys
from Monad import Monad
from itertools import product

with open(sys.argv[1]) as f:
    pgm = [line.rstrip() for line in f]

step = 0
best = -1
for pr in product(range(1,10), repeat=14):
    step += 1
    if step % 100_000 == 0:
        print(f'{step=}, {best=}')
    
    monad = Monad(pgm, pr)
    monad.run()
    if monad.reg['z'] == 0:
        print(pr, monad.reg['z'])
        best = ''.join(pr)
