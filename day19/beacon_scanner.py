import sys
from itertools import permutations, product
from collections import defaultdict

def orientations():
    for perm in permutations(range(3)):
        for prd in product([-1,1], repeat=2):
            yield perm[0], perm[1], perm[2], prd[0], prd[1]

# generate set of intrabeacon offsets
def gen_offsets(coords):
    offsets = set()
    pairs = dict()
    for i in range(len(coords)-1):
        for j in range(i+1, len(coords)):
            vals = (coords[i][0] - coords[j][0],
                    coords[i][1] - coords[j][1],
                    coords[i][2] - coords[j][2])
            offsets.add(vals)
            pairs[vals] = (i,j)
    return offsets, pairs

# def match_offsets(matched, scanner):
#     for x,y,z,p1,p2 in orientations():
#         # find the offsets and pairs for this orientation
#         coords = [(arr[x], arr[y] * p1, arr[z] * p2) for arr in scanner]
#         offsets, pairs = gen_offsets(coords)

#         # check if the offsets match anything we're already found
#         for match in matched:
#             good_idx, good_offsets, good_pairs = match
#             if (good_offsets & offsets):
#                 overlap = set()
#                 for triple in good_offsets & offsets:
#                     for offset in pairs[triple]:
#                         overlap.add(offset)
#                 if len(overlap) >= 12:
#                     # convert the overlap
#                     return good_idx, overlap, x, y, z, p1, p2


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

unmatched = {i for i in range(1, len(scanners))}
matched = {0}

offsets, pairs = gen_offsets(scanners[0])
#matched = [(0, offsets, pairs)] 
beacons = set()
deltas = {0: (0,0,0)}
orients = {0: (0,1,2,1,1)}

while unmatched:
    to_remove = set()
    for idx1 in unmatched:
        sc1 = scanners[idx1]
        done = False
        for idx0 in matched:
            if done:
                break
            print(f'testing {idx0} vs {idx1}')
            sc0 = scanners[idx0]
            gx,gy,gz,gp1,gp2 = orients[idx0]
            for x,y,z,p1,p2 in orientations():
                if done:
                    break
                cnt = defaultdict(list)
                for t0 in sc0:
                    for t1 in sc1:
#                        trip = (t1[x] + t0[gx], t1[y] * p1 + t0[gy] * gp1, t1[z] * p2 + t0[gz] * gp2)
                        trip = (t1[x] + t0[gx], t1[y] * p1 + t0[gy],  t1[z] * p2 + t0[gz])
                        cnt[trip].append((t0[0], t0[1], t0[2]))
                for k,v in cnt.items():
                    if len(v) >= 12:
                        print(k, v)
                        to_remove.add(idx1)
                        deltas[idx1] = k
                        orients[idx1] = (x,y,z,p1,p2)
                        done = True
    if not to_remove:
        print("nothing to remove!")
        break
    unmatched -= to_remove
    for x in to_remove:
        matched.add(x)
#        dx,dy,dz = deltas[x]
#        normalized_scan = [(x + dx, y+dy, z+dz) for x,y,z in scanners[x]]
#        scanners[x] = normalized_scan

# sc0 = scanners[0]
# sc1 = scanners[1]
# for x,y,z,p1,p2 in orientations():
#     cnt = defaultdict(list)
#     for t0 in sc0:
#         for t1 in sc1:
#             trip = (t1[x] + t0[0], t1[y] * p1 + t0[1], t1[z] * p2 + t0[2])
#             cnt[trip].append((t0[0], t0[1], t0[2]))
#         for k,v in cnt.items():
#             if len(v) >= 12:
#                 print(k, v)
#                 break
# #        print(cnt)

# while unmatched:
#     to_remove = set()
#     for idx in unmatched:
#         for x,y,z,p1,p2 in orientations():
#             # find the offsets and pairs for this orientation
#             coords = [(arr[x], arr[y] * p1, arr[z] * p2) for arr in scanners[idx]]
#             offsets, pairs = gen_offsets(coords)

#             # check if the offsets match anything we're already found
#             for match in matched:
#                 good_idx, good_offsets, good_pairs = match
#                 if (good_offsets & offsets):
#                     overlap = set()
#                     for triple in good_offsets & offsets:
#                         for offset in pairs[triple]:
#                             overlap.add(offset)
#                     if len(overlap) >= 12:
#                         # get the location of scanner idx relative to scanner good_idx
#                         triple = list(good_offsets & offsets)[0]
#                         good_offset = good_pairs[triple]
#                         new_offset = pairs[triple]
#         break
#     break

# for x,y,z,p1,p2 in orientations():
#     coords = [(arr[x], arr[y] * p1, arr[z] * p2) for arr in scanners[1]]
#     s1,off1 = gen_offsets(coords)
#     print(len(s0 & s1))
#     overlap = set()
#     if (len(s0 & s1) >= 28):
#         for triple in s0 & s1:
#             for offset in off0[triple]:
#                 overlap.add(offset)
#         print(overlap)
#         print(x,y,z,p1,p2)
