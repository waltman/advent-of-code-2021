import sys

POINTS = { ')': 3,
           ']': 57,
           '}': 1197,
           '>': 25137,
         }

MATCH = {')': '(',
         ']': '[',
         '}': '{',
         '>': '<',
        }

error_score = 0
with open(sys.argv[1]) as f:
    for line in f:
        stack = []
        for c in line.rstrip():
            if c in MATCH:
                if len(stack) == 0 or stack[-1] != MATCH[c]:
                    error_score += POINTS[c]
                    break
                else:
                    stack.pop()
            else:
                stack.append(c)
print('Part 1:', error_score)

