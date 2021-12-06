import sys

day = 0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip()
        fish = [0] * 9
        for x in map(int, line.split(',')):
            fish[x] += 1
        print(day, fish, line.rstrip())
        day += 1
