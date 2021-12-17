import sys
from math import prod

version_sum = 0

def op_sum(arr):
    return sum(arr)

def op_prod(arr):
    return prod(arr)

def op_min(arr):
    return min(arr)

def op_max(arr):
    return max(arr)

def op_gt(arr):
    return 1 if arr[0] > arr[1] else 0

def op_lt(arr):
    return 1 if arr[0] < arr[1] else 0

def op_eq(arr):
    return 1 if arr[0] == arr[1] else 0

def decode_literal(packet, i):
    bits = ''
    while True:
        flag = packet[i]; i += 1
        bits += packet[i:i+4]; i += 4
        if flag == '0':
            break
    val = int(bits, 2)
    print(f'{val=}')
    return i, val

def decode_operator(packet, i, op):
    print('decode_operator')
    length_type = packet[i]; i += 1
    arr = []
    if length_type == '0':
        subpacket_len = int(packet[i:i+15], 2); i += 15
        print(f'{subpacket_len=}')
        end = i + subpacket_len
        while i < end:
            i, val = decode_packet(packet, i)
            arr.append(val)
    else:
        num_subpackets = int(packet[i:i+11], 2); i += 11
        print(f'{num_subpackets=}')
        for j in range(num_subpackets):
            print(f'{j=}')
            i, val = decode_packet(packet, i)
            arr.append(val)
    return i, op(arr)

def decode_packet(packet, i):
    global version_sum
    
    op = {0: op_sum,
          1: op_prod,
          2: op_min,
          3: op_max,
          5: op_gt,
          6: op_lt,
          7: op_eq,
          }

    version = int(packet[i:i+3], 2); i += 3
    version_sum += version
    print(f'{version=}')
    type_id = int(packet[i:i+3], 2); i += 3
    print(f'{type_id=}')
    if type_id == 4:
        i, res = decode_literal(packet, i)
    else:
        i, res = decode_operator(packet, i, op[type_id])
        print(f'{i=}')

    return i, res

with open(sys.argv[1]) as f:
    packet = ''.join([f'{int(c,16):04b}' for c in f.readline().rstrip()])

i, res = decode_packet(packet, 0)

print('Part 1:', version_sum)
print('Part 2:', res)
