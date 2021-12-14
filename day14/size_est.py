import sys
size = len(sys.argv[1])
for step in range(40):
    size = size * 2 - 1
    print(step+1, size)
