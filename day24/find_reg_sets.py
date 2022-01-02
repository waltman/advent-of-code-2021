import sys
from Monad import Monad
from itertools import product
from collections import defaultdict

with open('input.txt') as f:
    pgm = [line.rstrip() for line in f]

regsets = [(0,0,0,0)]

for i in range(14):
    reg_set = defaultdict(int)
    for pr in range(1, 10):
        monad = Monad(pgm[i*18:(i+1)*18], [pr])
        for regs in regsets:
            monad.reset()
            monad.reg['w'] = regs[0]
            monad.reg['x'] = regs[1]
            monad.reg['y'] = regs[2]
            monad.reg['z'] = regs[3]
            monad.run()
            k = (monad.reg['w'],monad.reg['x'],monad.reg['y'],monad.reg['z'])
            reg_set[k] += 1
    print(f'{i=} {len(reg_set)=}')
    # find the tuples that occurred least frequently
    best_cnt = float('Inf')
    best_tuples = []
    for k,v in reg_set.items():
        if v < best_cnt:
            best_cnt = v
            best_tuples = [k]
        elif v == best_cnt:
            best_tuples.append(k)
    regsets = best_tuples

for regs in regsets:
    if regs[3] == 0:
        print(regs)
