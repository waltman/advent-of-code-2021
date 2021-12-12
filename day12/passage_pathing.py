import sys
from collections import defaultdict

# parse the input
neighbors = defaultdict(set)
with open(sys.argv[1]) as f:
    for line in f:
        (n1, n2) = line.rstrip().split('-')
        neighbors[n1].add(n2)
        neighbors[n2].add(n1)

# remove backlinks to start
for neighbor in neighbors.values():
    if 'start' in neighbor:
        neighbor.remove('start')

# find the paths
paths = 0
stack = [('start', set())]
while stack:
    node, smalls = stack.pop()
    if node == 'end':
        paths += 1
    else:
        for neighbor in neighbors[node]:
            if neighbor.isupper():
                stack.append((neighbor, smalls))
            elif neighbor not in smalls:
                stack.append((neighbor, smalls | set([neighbor])))
print('Part 1:', paths)

# find the paths for part 2
paths = 0
stack = [('start', set(), True)]
while stack:
    node, smalls, dupe_ok = stack.pop()
    if node == 'end':
        paths += 1
    else:
        for neighbor in neighbors[node]:
            if neighbor.isupper():
                stack.append((neighbor, smalls, dupe_ok))
            elif neighbor not in smalls:
                stack.append((neighbor, smalls | set([neighbor]), dupe_ok))
            elif dupe_ok:
                stack.append((neighbor, smalls, False))
print('Part 2:', paths)
