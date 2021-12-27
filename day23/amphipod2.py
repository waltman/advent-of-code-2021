import sys
from functools import cache

def clear_path(grid, from_col, to_col):
    delta = 1 if from_col < to_col else -1
    i = from_col + delta
    while True:
        if grid[1][i] != '.':
            return False
        elif i == to_col:
            return True
        else:
            i += delta

def homeable(grid, ch, col):
    # there should be nothing but . and ch in this column
    match = set(['.', ch])
    for row in range(2,6):
        if grid[row][col] not in match:
            return False
    return True

def home_row(grid, col):
    for row in range(5, 1, -1):
        if grid[row][col] == '.':
            return row

@cache
def valid_moves(diagram, row, col, ch):
    cost = {'A': 1,
            'B': 10,
            'C': 100,
            'D': 1000}
    home_col = {'A': 3,
                'B': 5,
                'C': 7,
                'D': 9}

    if ch not in cost:
        return []

    grid = diagram.split('\n')

    # can we move it home?
    if homeable(grid, ch, home_col[ch]):
        new_row = home_row(grid, home_col[ch])
        vert = (row-1) + (new_row-1)
        horz = abs(col-home_col[ch])
        return [(ch, row, col, 3, home_col[ch], cost[ch] * (vert + horz))]
    elif row == 1:
        return []

    # find all the corridors
    moves = []
    
    # check left
    new_col = col-1
    while grid[1][new_col] == '.':
        moves.append((ch, row, col, 1, new_col, cost[ch] * ((row-1) + (col-new_col))))
        new_col -= 1

    # check right
    new_col = col+1
    while grid[1][new_col] == '.':
        moves.append((ch, row, col, 1, new_col, cost[ch] * ((row-1) + (new_col-col))))
        new_col += 1

    return moves

def moveable(grid, ch, row, col):
    home_col = {'A': 3,
                'B': 5,
                'C': 7,
                'D': 9}

    if ch not in home_col:
        return False

    if col == home_col[ch]:
        # if something above is isn't a ., they're we're stuck
        for r in range(2, row):
            if grid[r][col] != '.':
                return False

        # everything below it should be ch
        for r in range(row+1, 6):
            if grid[r][col] != ch:
                return True
        return False
    else:
        # if something above is isn't a ., they're we're stuck
        for r in range(2, row):
            if grid[r][col] != '.':
                return False
        return True

@cache
def best_solution(diagram, energy):
    grid = diagram.split('\n')

    # do we have a solution?
    if grid[2][3] == 'A' and grid[3][3] == 'A' and grid[4][3] == 'A' and grid[5][3] == 'A' and \
       grid[2][5] == 'B' and grid[3][5] == 'B' and grid[4][5] == 'B' and grid[5][5] == 'B' and \
       grid[2][7] == 'C' and grid[3][7] == 'C' and grid[4][7] == 'C' and grid[5][7] == 'C' and \
       grid[2][9] == 'D' and grid[3][9] == 'D' and grid[4][9] == 'D' and grid[5][9] == 'D':
       return energy

    # find all the possible moves
    moves = []
    # check columns
    for ch, col in [('A', 3), ('B', 5), ('C', 7), ('D', 9)]:
        for row in range(2, 6):
            if moveable(grid, grid[row][col], row, col):
                moves += valid_moves(diagram, row, col, grid[row][col])
                break
            
    # corridor
    for col in range(len(grid[1])):
        if grid[1][col] in set(['A','B','C','D']):
            moves += valid_moves(diagram, 1, col, grid[1][col])

    best_score = float('Inf')
    for move in moves:
        ch, row1, col1, row2, col2, cost = move
        new_grid = grid.copy()

        tmp = list(new_grid[row1])
        tmp[col1] = '.'
        new_grid[row1] = ''.join(tmp)

        tmp = list(new_grid[row2])
        tmp[col2] = ch
        new_grid[row2] = ''.join(tmp)

        new_diagram = '\n'.join(new_grid)
        best_score = min(best_score, best_solution(new_diagram, energy + cost))
    return best_score
            

# parse the input
with open(sys.argv[1]) as f:
    diagram = ''.join(f.readlines())

# add the 2 new lines
diagram = diagram[0:42] + '  #D#C#B#A#\n  #D#B#A#C#\n' + diagram[42:]

print('Part 2:', best_solution(diagram, 0))

