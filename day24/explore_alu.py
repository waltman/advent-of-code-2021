import sys
from Monad import Monad
from itertools import product
from collections import defaultdict

with open('input.txt') as f:
    pgm = [line.rstrip() for line in f]

length = int(sys.argv[1])
states = defaultdict(list)
step = 0
for pr in product(range(9,0,-1), repeat=length):
    step += 1
    
    monad = Monad(pgm[0:length*18], pr)
    monad.run()

    k = f"{monad.reg['w']},{monad.reg['x']},{monad.reg['y']},{monad.reg['z']}"
    states[k].append(pr)

print(f'{step=}, {len(states)=}')
counts = defaultdict(int)
for v in states.values():
    counts[len(v)] += 1
print(counts)
for k,v in states.items():
    if len(v) == 2:
        print(k, v)

