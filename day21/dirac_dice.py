import sys

class D100:
    def __init__(self):
        self.d100 = 1
        self.rolls = 0

    def roll(self):
        val = 0
        for _ in range(3):
            val = self.d100
            self.d100 += 1
            if self.d100 == 101:
                self.d100 = 1
        self.rolls += 1
        return val

# parse input
with open(sys.argv[1]) as f:
    p1 = int(f.readline().rstrip()[-1]) - 1
    p2 = int(f.readline().rstrip()[-1]) - 1

d100 = D100()
ps1 = 0
ps2 = 0

while True:
    p1 = (p1 + d100.roll()) % 10
    ps1 += p1 + 1
    if ps1 >= 1000:
        break

    p2 = (p2 + d100.roll()) % 10
    ps2 += p2 + 1
    if ps2 >= 1000:
        break

    break
print(p1, ps1, p2, ps2)
