import sys
import re

cnt = 0
uniq_lens = {2, 4, 3, 7}
with open(sys.argv[1]) as f:
    for line in f:
        m = re.match(r'(.*) \| (.*)', line.rstrip())
        toks = m.group(2).split(' ')
        for tok in toks:
            if len(tok) in uniq_lens:
                cnt += 1
print('Part 1:', cnt)

