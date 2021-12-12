import sys
from queue import Queue
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
q = Queue()
q.put(('start', set()))
while not q.empty():
    node, smalls = q.get()
    if node == 'end':
        paths += 1
    else:
        for neighbor in neighbors[node]:
            if neighbor.isupper():
                q.put((neighbor, smalls))
            elif neighbor not in smalls:
                q.put((neighbor, smalls | set([neighbor])))
print('Part 1:', paths)

# find the paths for part 2
paths = 0
q = Queue()
q.put(('start', set(), True))
while not q.empty():
    node, smalls, dupe_ok = q.get()
    if node == 'end':
        paths += 1
    else:
        for neighbor in neighbors[node]:
            if neighbor.isupper():
                q.put((neighbor, smalls, dupe_ok))
            elif neighbor not in smalls:
                q.put((neighbor, smalls | set([neighbor]), dupe_ok))
            elif dupe_ok:
                q.put((neighbor, smalls, False))
print('Part 2:', paths)
