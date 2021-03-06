import sys
from math import prod

version_sum = 0

def decode_literal(packet, i):
    bits = ''
    while True:
        flag = packet[i]; i += 1
        bits += packet[i:i+4]; i += 4
        if flag == '0':
            break
    val = int(bits, 2)
    return i, val

def decode_operator(packet, i, op):
    length_type = packet[i]; i += 1
    arr = []
    if length_type == '0':
        subpacket_len = int(packet[i:i+15], 2); i += 15
        end = i + subpacket_len
        while i < end:
            i, val = decode_packet(packet, i)
            arr.append(val)
    else:
        num_subpackets = int(packet[i:i+11], 2); i += 11
        for j in range(num_subpackets):
            i, val = decode_packet(packet, i)
            arr.append(val)
    return i, op(arr)

def decode_packet(packet, i):
    global version_sum
    
    op = {0: lambda a: sum(a),
          1: lambda a: prod(a),
          2: lambda a: min(a),
          3: lambda a: max(a),
          5: lambda a: 1 if a[0] > a[1] else 0,
          6: lambda a: 1 if a[0] < a[1] else 0,
          7: lambda a: 1 if a[0] == a[1] else 0,
          }

    version = int(packet[i:i+3], 2); i += 3
    version_sum += version
    type_id = int(packet[i:i+3], 2); i += 3
    if type_id == 4:
        i, res = decode_literal(packet, i)
    else:
        i, res = decode_operator(packet, i, op[type_id])

    return i, res

with open(sys.argv[1]) as f:
    packet = ''.join([f'{int(c,16):04b}' for c in f.readline().rstrip()])

i, res = decode_packet(packet, 0)

print('Part 1:', version_sum)
print('Part 2:', res)
