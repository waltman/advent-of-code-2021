import sys
from collections import defaultdict

# parse input
rules = {}
with open(sys.argv[1]) as f:
    polymer = f.readline().rstrip()
    f.readline()
    for line in f:
        toks = line.rstrip().split(' -> ')
        rules[toks[0]] = toks[1]

# apply rules
for step in range(1,11):
    tmp = ''
    for i in range(len(polymer)-1):
        tmp += polymer[i] + rules[polymer[i:i+2]]
    polymer = tmp + polymer[-1]

# compute part 1
counts = defaultdict(int)
for c in polymer:
    counts[c] += 1
print('Part 1:', max(counts.values()) - min(counts.values()))
