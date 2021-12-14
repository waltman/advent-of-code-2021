import sys
from collections import defaultdict

def compute_score(num_pairs):
    counts = defaultdict(int)
    for k,v in num_pairs.items():
        for c in k:
            if c != ' ':
                counts[c] += v / 2
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
num_pairs = defaultdict(int)
for i in range(len(polymer)-1):
    num_pairs[polymer[i:i+2]] += 1

# add extra pairs for the front and back
num_pairs[' ' + polymer[0]] = num_pairs[polymer[-1] + ' '] = 1

# apply rules
for step in range(1,41):
    new_num_pairs = defaultdict(int)
    for pair in num_pairs.keys():
        if pair in rules:
            rule = rules[pair]
            new_num_pairs[pair[0] + rule] += num_pairs[pair]
            new_num_pairs[rule + pair[1]] += num_pairs[pair]
        else:
            new_num_pairs[pair] = 1
    num_pairs = new_num_pairs
    if step == 10:
        print('Part 1:', compute_score(num_pairs))
    elif step == 40:
        print('Part 2:', compute_score(num_pairs))
