import sys

def cost(x, y):
    dist = abs(x-y)
    return sum(range(dist+1))

with open(sys.argv[1]) as f:
    crabs = [int(x) for x in f.readline().split(',')]

best_pos = 0
best_fuel = 1e300
for pos in range(min(crabs), max(crabs)):
    if (fuel := sum([abs(crabs[i] - pos) for i in range(len(crabs))])) < best_fuel:
        best_pos = pos
        best_fuel = fuel
print('Part 1:', best_fuel)

best_pos = 0
best_fuel = 1e300
for pos in range(min(crabs), max(crabs)):
    if (fuel := sum([cost(crabs[i], pos) for i in range(len(crabs))])) < best_fuel:
        best_pos = pos
        best_fuel = fuel
print('Part 2:', best_fuel)

