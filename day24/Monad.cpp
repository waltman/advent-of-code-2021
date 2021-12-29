#include <ctype.h>
#include <string>
#include "Monad.h"

bool is_numeric(const string str) {
    for (char c : str) {
        if (!(isdigit(c) || c == '-'))
            return false;
    }
    return true;
}

Monad::Monad(vector<string> pgm, int *input, size_t size) {
    _pgm = pgm;
    _input = input;
    _size = size;
    inp_ptr = 0;
    reg['x'] = 0;
    reg['y'] = 0;
    reg['z'] = 0;
    reg['w'] = 0;
}

void Monad::do_inp(const char a) {
    reg[a] = _input[inp_ptr++];
}

void Monad::do_add(const char a, const string b) {
    if (is_numeric(b))
        reg[a] += stoll(b);
    else
        reg[a] += reg[b[0]];
}

void Monad::do_mul(const char a, const string b) {
    if (is_numeric(b))
        reg[a] *= stoll(b);
    else
        reg[a] *= reg[b[0]];
}

void Monad::do_div(const char a, const string b) {
    if (is_numeric(b))
        reg[a] /= stoll(b);
    else
        reg[a] /= reg[b[0]];
}

void Monad::do_mod(const char a, const string b) {
    if (is_numeric(b))
        reg[a] %= stoll(b);
    else
        reg[a] %= reg[b[0]];
}

void Monad::do_eql(const char a, const string b) {
    long long val = is_numeric(b) ? stoll(b) : reg[b[0]];
    reg[a] = (reg[a] == val) ? 1 : 0;
}
            
