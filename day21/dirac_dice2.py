import sys
from itertools import product
from collections import defaultdict
from functools import cache

board = list(range(1,11)) * 100

@cache
def game(player1, player2, turn):
    player = player1 if turn == 0 else player2
    pos, score = player
    victories = 0
    state = defaultdict(int)
    for pr in product(range(1,4), repeat=3):
        new_pos = pos + sum(pr)
        new_score = score + board[new_pos]
        if new_score >= 21:
            victories += 1
        else:
            state[(new_pos, new_score)] += 1

    if turn == 0:
        (wins, losses) = (victories, 0)
        for k,v in state.items():
            w,l = game(k, player2, 1)
            wins += w * v
            losses += l * v
    else:
        (wins, losses) = (0, victories)
        for k,v in state.items():
            w,l = game(player1, k, 0)
            wins += w * v
            losses += l * v
    return wins, losses

# parse input
with open(sys.argv[1]) as f:
    p1 = int(f.readline().rstrip()[-1]) - 1
    p2 = int(f.readline().rstrip()[-1]) - 1

(wins, losses) = game((p1, 0), (p2, 0), 0)
print('Part 2', max(wins, losses))
