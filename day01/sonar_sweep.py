import sys

def count_larger(a):
    cnt = 0
    for i in range(1, len(a)):
        if a[i] > a[i-1]:
            cnt += 1
    return cnt

with open(sys.argv[1]) as f:
    depth = [int(line) for line in f.readlines()]

print('Part 1:', count_larger(depth))

# compute sliding windows
windows = [sum(depth[i:i+3]) for i in range(0, len(depth)-2)]
print('Part 2:', count_larger(windows))
