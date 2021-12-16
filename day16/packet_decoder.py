import sys

with open(sys.argv[1]) as f:
    line = f.readline().rstrip()
    packet = ''
    for c in line:
        packet += f'{int(c,16):04b}'

