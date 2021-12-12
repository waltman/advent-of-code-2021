import sys
import networkx as nx
from queue import Queue
from collections import defaultdict

# parse the input
G = nx.Graph()
with open(sys.argv[1]) as f:
    for line in f:
        (n1, n2) = line.rstrip().split('-')
        G.add_edge(n1, n2)

# find the paths
paths = []
q = Queue()
q.put(('start', ['start']))
while not q.empty():
    node, path = q.get()
    if node == 'end':
        paths.append(path.copy())
    else:
        for neighbor in G.adj[node]:
            if neighbor.isupper() or (neighbor.islower() and neighbor not in path):
                q.put((neighbor, path + [neighbor]))
print('Part 1:', len(paths))

# find the paths for part 2
paths = []
q = Queue()
q.put(('start', ['start'], set(), True))
while not q.empty():
    node, path, smalls, dupe_ok = q.get()
    if node == 'end':
        paths.append(path.copy())
    else:
        for neighbor in filter(lambda s: s != 'start', G.adj[node]):
            if neighbor.isupper():
                q.put((neighbor, path + [neighbor], smalls, dupe_ok))
            elif neighbor not in smalls:
                q.put((neighbor, path + [neighbor], smalls | set([neighbor]), dupe_ok))
            elif dupe_ok:
                q.put((neighbor, path + [neighbor], smalls, False))
print('Part 2:', len(paths))
