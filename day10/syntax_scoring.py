import sys

POINTS = { ')': 3,
           ']': 57,
           '}': 1197,
           '>': 25137,
         }

MATCH = {k:v for k,v in zip("()[]{}<>", ")(][}{><")}

AUTOCOMPLETE_POINTS = {c: i+1 for i,c in enumerate(")]}>")}

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
            while stack:
                c = stack.pop()
                score = 5 * score + AUTOCOMPLETE_POINTS[MATCH[c]]
            autocomplete_scores.append(score)
print('Part 1:', error_score)
print('Part 2:', sorted(autocomplete_scores)[len(autocomplete_scores)//2])
