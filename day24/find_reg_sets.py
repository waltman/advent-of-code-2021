import sys
from Monad import Monad
from itertools import product
from collections import defaultdict

with open('input.txt') as f:
    pgm = [line.rstrip() for line in f]

regsets = [set([(0,0,0,0)])]

for i in range(14):
    reg_set = set()
    for pr in range(1, 10):
        monad = Monad(pgm[i*18:(i+1)*18], [pr])
        for regs in regsets[i]:
            monad.reset()
            monad.reg['w'] = regs[0]
            monad.reg['x'] = regs[1]
            monad.reg['y'] = regs[2]
            monad.reg['z'] = regs[3]
            monad.run()
            k = (monad.reg['w'],monad.reg['x'],monad.reg['y'],monad.reg['z'])
            reg_set.add(k)
    print(f'{i=} {len(reg_set)=}')
    regsets.append(reg_set)

for regs in regsets[-1]:
    if regs[3] == 0:
        print(regs)
