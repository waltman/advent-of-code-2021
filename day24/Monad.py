class Monad:
    def __init__(self, pgm, _input):
        self.pgm = pgm
        self._input = _input
        self.ip = 0
        self.inp_ptr = 0
        self.reg = {'x': 0,
                    'y': 0,
                    'z': 0,
                    'w': 0}
        self.ops = {
            'inp': self.do_inp,
            'add': self.do_add,
            'mul': self.do_mul,
            'div': self.do_div,
            'mod': self.do_mod,
            'eql': self.do_eql,
        }

    # def get_inp(self):
    #     for val in self._input:
    #         yield val

    def do_inp(self, a):
        val = self._input[self.inp_ptr]
        self.inp_ptr += 1
        self.reg[a] = val

    def do_add(self, a, b):
        if b.lstrip('-').isdigit():
            self.reg[a] += int(b)
        else:
            self.reg[a] += self.reg[b]

    def do_mul(self, a, b):
        if b.lstrip('-').isdigit():
            self.reg[a] *= int(b)
        else:
            self.reg[a] *= self.reg[b]

    def do_div(self, a, b):
        if b.lstrip('-').isdigit():
            self.reg[a] = self.reg[a] // int(b)
        else:
            self.reg[a] = self.reg[a] // self.reg[b]

    def do_mod(self, a, b):
        if b.lstrip('-').isdigit():
            self.reg[a] = self.reg[a] % int(b)
        else:
            self.reg[a] = self.reg[a] % self.reg[b]

    def do_eql(self, a, b):
        val = int(b) if b.lstrip('-').isdigit() else self.reg[b]
        self.reg[a] = 1 if self.reg[a] == val else 0

    def run(self):
        for self.ip in range(len(self.pgm)):
#            print(self.pgm[self.ip])
            toks = self.pgm[self.ip].split()
            if toks[0] == 'inp':
                self.do_inp(toks[1])
            else:
                self.ops[toks[0]](toks[1], toks[2])
#            print(self.reg)
#        print(self.reg)
