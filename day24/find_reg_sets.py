import sys
from Monad import Monad
from itertools import product
from collections import defaultdict

with open(sys.argv[1]) as f:
    pgm = [line.rstrip() for line in f]

regsets = [(0,0,0,0,[])]

for i in range(14):
    reg_set = defaultdict(int)
    prs = defaultdict(list)
    for pr in range(1, 10):
        monad = Monad(pgm[i*18:(i+1)*18], [pr])
        for w,x,y,z,arr in regsets:
            monad.reset()
            monad.reg['w'] = w
            monad.reg['x'] = x
            monad.reg['y'] = y
            monad.reg['z'] = z
            monad.run()
            if len(arr) == 0:
                new_arr = [pr]
            else:
                new_arr = [x * 10 + pr for x in arr]
            k = (monad.reg['w'],monad.reg['x'],monad.reg['y'],monad.reg['z'])
            reg_set[k] += 1
            prs[k] += new_arr
    print(f'{i=} {len(reg_set)=}')
    # find the tuples that occurred least frequently
    best_cnt = float('Inf')
    best_tuples = []
    for k,v in reg_set.items():
        w,x,y,z = k
        if v < best_cnt:
            best_cnt = v
            best_tuples = [(w,x,y,z,prs[k])]
        elif v == best_cnt:
            best_tuples.append((w,x,y,z,prs[k]))
    regsets = best_tuples

valid = []
for regs in regsets:
    if regs[3] == 0:
        valid += regs[4]
print('Part 1:', sorted(valid)[-1])
print('Part 2:', sorted(valid)[0])
print(f'There are a total of {len(valid)} solutions.')
