import sys
import re
from itertools import permutations

cnt = 0
tot = 0
uniq_lens = {2, 4, 3, 7}
DISPLAY = ['abcefg',
           'cf',
           'acdeg',
           'acdfg',
           'bcdf',
           'abdfg',
           'abdefg',
           'acf',
           'abcdefg',
           'abcdfg',
]

def get_mapping(display, inputs):
    for perm in permutations(range(7)):
        remapping = {'abcdefg'[i] : 'abcdefg'[perm[i]] for i in range(7)}
        mapping = [{remapping[c] for c in d} for d in display]
        found = True
        for tok in inputs:
            tokset = set(tok)
            if tokset not in mapping:
                found = False
                break
        if found:
            return mapping

with open(sys.argv[1]) as f:
    for line in f:
        m = re.match(r'(.*) \| (.*)', line.rstrip())
        inputs = m.group(1).split(' ')
        outputs = m.group(2).split(' ')
        for tok in outputs:
            if len(tok) in uniq_lens:
                cnt += 1
        mapping = get_mapping(DISPLAY, inputs)
        val = 0
        for tok in outputs:
            tokset = set(tok)
            for i in range(len(mapping)):
                if tokset == mapping[i]:
                    val *= 10
                    val += i
                    break
        tot += val
print('Part 1:', cnt)
print('Part 2:', tot)
