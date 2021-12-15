import sys
import networkx as nx

# parse the input
with open(sys.argv[1]) as f:
    grid = [[int(c) for c in line.rstrip()] for line in f]
num_rows = len(grid)
num_cols = len(grid[0])

# convert to digraph
DG = nx.DiGraph()
# rows
for row in range(num_rows):
    for col in range(num_cols-1):
        DG.add_weighted_edges_from([((row,col),(row,col+1),grid[row][col+1])])
        DG.add_weighted_edges_from([((row,col+1),(row,col),grid[row][col])])
# cols
for col in range(num_cols):
    for row in range(num_rows-1):
        DG.add_weighted_edges_from([((row,col),(row+1,col),grid[row+1][col])])
        DG.add_weighted_edges_from([((row+1,col),(row,col),grid[row][col])])

# find distance
print(nx.dijkstra_path_length(DG, (0,0), (num_rows-1,num_cols-1)))
