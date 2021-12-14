import sys
from collections import defaultdict

def compute_score(pairs):
    counts = defaultdict(int)
    for k in pairs:
        for c in k:
            if c != ' ':
                counts[c] += pairs[k] / 2
    return int(max(counts.values()) - min(counts.values()))

# parse input
rules = {}
with open(sys.argv[1]) as f:
    polymer = f.readline().rstrip()
    f.readline()
    for line in f:
        toks = line.rstrip().split(' -> ')
        rules[toks[0]] = toks[1]

# count initial pairs
pairs = defaultdict(int)
for i in range(len(polymer)-1):
    pairs[polymer[i:i+2]] += 1

# add extra pairs for the front and back
pairs[' ' + polymer[0]] = pairs[polymer[-1] + ' '] = 1

# apply rulss
for step in range(1,41):
    new_pairs = defaultdict(int)
    for pair in pairs:
        if pair in rules:
            rule = rules[pair]
            new_pairs[pair[0] + rule] += pairs[pair]
            new_pairs[rule + pair[1]] += pairs[pair]
        else:
            new_pairs[pair] = 1
    pairs = new_pairs
    if step == 10:
        print('Part 1:', compute_score(pairs))
    elif step == 40:
        print('Part 2:', compute_score(pairs))
