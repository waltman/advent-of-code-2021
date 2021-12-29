import sys
from Monad import Monad
from itertools import product
from random import randint

with open(sys.argv[1]) as f:
    pgm = [line.rstrip() for line in f]

monad = Monad(pgm, [])
for pr in product(range(0,10), repeat=2):
    monad.reset()
    monad._input = pr
    monad.run()
    print(list(pr), monad.reg)
