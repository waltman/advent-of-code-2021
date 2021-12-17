import sys

version_sum = 0

def decode_literal(packet, i):
    bits = ''
    while True:
        flag = packet[i]; i += 1
        bits += packet[i:i+4]; i += 4
        if flag == '0':
            break
    val = int(bits, 2)
    print(f'{val=}')
    return i

def decode_operator(packet, i):
    print('decode_operator')
    length_type = packet[i]; i += 1
    if length_type == '0':
        subpacket_len = int(packet[i:i+15], 2); i += 15
        print(f'{subpacket_len=}')
        end = i + subpacket_len
        while i < end:
            i = decode_packet(packet, i)
    else:
        num_subpackets = int(packet[i:i+11], 2); i += 11
        print(f'{num_subpackets=}')
        for j in range(num_subpackets):
            print(f'{j=}')
            i = decode_packet(packet, i)
    return i

def decode_packet(packet, i):
    global version_sum
    
    version = int(packet[i:i+3], 2); i += 3
    version_sum += version
    print(f'{version=}')
    type_id = int(packet[i:i+3], 2); i += 3
    print(f'{type_id=}')
    if type_id == 4:
        i = decode_literal(packet, i)
    else:
        i = decode_operator(packet, i)
        print(f'{i=}')

    return i

with open(sys.argv[1]) as f:
    packet = ''.join([f'{int(c,16):04b}' for c in f.readline().rstrip()])

decode_packet(packet, 0)

print('Part 1:', version_sum)
