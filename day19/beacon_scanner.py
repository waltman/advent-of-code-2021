import sys
from itertools import permutations, product

def orientations():
    for perm in permutations(range(3)):
        for prd in product([-1,1], repeat=2):
            yield perm[0], perm[1], perm[2], prd[0], prd[1]

# generate set of intrabeacon offsets
def gen_offsets(coords):
    offsets = set()
    for i in range(len(coords)-1):
        for j in range(i+1, len(coords)):
            offsets.add((abs(coords[i][0] - coords[j][0]),
                         abs(coords[i][1] - coords[j][1]),
                         abs(coords[i][2] - coords[j][2])))
    return offsets

# parse input
scanners = []
coords = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip()
        if line[0:3] == '---': # skip
            continue
        elif line == '':
            scanners.append(coords)
            coords = []
        else:
            coords.append([int(x) for x in line.split(',')])
scanners.append(coords)

s0 = gen_offsets(scanners[0])
for x,y,z,p1,p2 in orientations():
    coords = [(arr[x], arr[y] * p1, arr[z] * p2) for arr in scanners[1]]
    s1 = gen_offsets(coords)
    print(len(s0 & s1))
