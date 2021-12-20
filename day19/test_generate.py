# test generating all the orientations
from itertools import permutations, product

def orientations(arr):
    for perm in permutations(range(3)):
        for prd in product([-1,1], repeat=2):
#            print(perm, prd)
            yield arr[perm[0]], arr[perm[1]]*prd[0], arr[perm[2]]*prd[1]

for x,y,z in orientations([1,2,3]):
    print(x,y,z)
