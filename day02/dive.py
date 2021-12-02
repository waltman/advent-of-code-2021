import sys

d, h = 0,0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip()
        cmd, val = line.split(' ')
        match(cmd):
            case 'forward':
                h += int(val)
            case 'down':
                d += int(val)
            case 'up':
                d -= int(val)

print('Part 1:', d * h)
