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
         '(': ')',
         '[': ']',
         '{': '}',
         '<': '>',
        }

AUTOCOMPLETE_POINTS = { ')': 1,
                        ']': 2,
                        '}': 3,
                        '>': 4,
                      }

error_score = 0
autocomplete_scores = []
with open(sys.argv[1]) as f:
    for line in f:
        stack = []
        for c in line.rstrip():
            if c in ')]}>':
                if len(stack) == 0 or stack[-1] != MATCH[c]:
                    error_score += POINTS[c]
                    stack = []
                    break
                else:
                    stack.pop()
            else:
                stack.append(c)
        if stack:
            score = 0
            for c in stack[::-1]:
                score += 5 * score + AUTOCOMPLETE_POINTS[MATCH[c]]
            autocomplete_scores.append(score)
print('Part 1:', error_score)
print('Part 2:', sorted(autocomplete_scores)[len(autocomplete_scores)//2])
