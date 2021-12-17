import sys

with open(sys.argv[1]) as f:
    packet = ''.join([f'{int(c,16):04b}' for c in f.readline().rstrip()])
