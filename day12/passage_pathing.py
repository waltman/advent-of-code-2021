import sys
import networkx as nx
from queue import Queue

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
