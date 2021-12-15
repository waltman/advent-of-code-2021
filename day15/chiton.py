import sys
import networkx as nx

def dist(grid, num_rows, num_cols):
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
    return nx.dijkstra_path_length(DG, (0,0), (num_rows-1,num_cols-1))

# parse the input
with open(sys.argv[1]) as f:
    grid = [[int(c) for c in line.rstrip()] for line in f]
num_rows = len(grid)
num_cols = len(grid[0])

print('Part 1:', dist(grid, num_rows, num_cols))

# expand first num_rows rows
for row in range(num_rows):
    for col in range(num_cols, num_cols*5):
        grid[row].append(1 if (val := grid[row][col-num_cols]) == 9 else val+1)

# add the remaining rows
for row in range(num_rows, num_rows*5):
    grid.append([1 if (val := grid[row-num_rows][col]) == 9 else val+1 for col in range(num_cols*5)])

print('Part 2:', dist(grid, num_rows*5, num_cols*5))
