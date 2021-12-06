import sys

fish = [0] * 9
with open(sys.argv[1]) as f:
    for x in map(int, f.readline().split(',')):
        fish[x] += 1

for day in range(256):
    tmp = fish[1:]
    tmp[6] += fish[0]
    tmp.append(fish[0])
    fish = tmp

    if day == 79:
        print('Part 1:', sum(fish))
    elif day == 255:
        print('Part 2:', sum(fish))
