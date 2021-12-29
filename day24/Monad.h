#ifndef MONAD_H
#define MONAD_H

#include <vector>
#include <map>
#include <cstddef>
#include <string>
#include <ostream>

using namespace std;

struct cmd {
    int op;
    char a;
    bool constant;
    long long b_val;
    char b_k;
};

class Monad {
private:
    vector<struct cmd> _pgm;
    int *_input;
    size_t inp_ptr;
    long long reg[4];

    void run_cmd(struct cmd command);

public:
    Monad(int *input);
    void run();
    void reset(int *input);
    long long get_reg(char a) { return reg[a-'w']; };
    void add_cmd(const string cmd);
};


inline ostream &operator<<(ostream &os, Monad monad) {
    return os << "w=" << monad.get_reg('w') <<
                " x=" << monad.get_reg('x') <<
                " y=" << monad.get_reg('y') <<
                " z=" << monad.get_reg('z');
}

#endif
