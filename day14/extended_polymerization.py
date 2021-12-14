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

print(pairs)
for step in range(1,5):
    new_pairs = defaultdict(int)
    for pair in pairs:
        rule = rules[pair]
        new_pairs[pair[0] + rule] += 1
        new_pairs[rule + pair[1]] += 1
    pairs = new_pairs
    print(step, pairs)
counts = defaultdict(int)
for c in 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB':
    counts[c] += 1
print('real', counts)

counts2 = defaultdict(int)
for k in pairs:
    for c in k:
        counts2[c] += pairs[k]
print('test', counts2)
print('NNCB -> NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')

