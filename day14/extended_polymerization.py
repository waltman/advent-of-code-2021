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
save_polymer = polymer
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

# compute part 2
pairs = defaultdict(int)
for i in range(len(save_polymer)-1):
    pairs[save_polymer[i:i+2]] += 1
pairs[' ' + save_polymer[0]] = 1
pairs[save_polymer[-1] + ' '] = 1

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

counts = defaultdict(int)
for k in pairs:
    for c in k:
        if c != ' ':
            counts[c] += pairs[k] / 2
print('Part 2:', int(max(counts.values()) - min(counts.values())))
