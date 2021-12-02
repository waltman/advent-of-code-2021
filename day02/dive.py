import sys

cmds = []
with open(sys.argv[1]) as f:
    for line in f:
        cmd, val = line.rstrip().split(' ')
        cmds.append((cmd, int(val)))

d,h = 0,0
for cmd,val in cmds:
    match(cmd):
        case 'forward':
            h += val
        case 'down':
            d += val
        case 'up':
            d -= val
print('Part 1:', d * h)

d,h,a = 0,0,0
for cmd,val in cmds:
    match(cmd):
        case 'forward':
            h += val
            d += a * val
        case 'down':
            a += val
        case 'up':
            a -= val
print('Part 2:', d * h)
