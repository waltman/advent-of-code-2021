#ifndef ODOMETER_H
#define ODOMETER_H

#include <vector>
#include <map>
#include <cstddef>
#include <string>

using namespace std;

class Monad {
private:
    vector<string> _pgm;
    int *_input;
    size_t _size;
    size_t inp_ptr;

    void do_inp(const char a);
    void do_add(const char a, const string b);
    void do_mul(const char a, const string b);
    void do_div(const char a, const string b);
    void do_mod(const char a, const string b);
    void do_eql(const char a, const string b);

public:
    map<char, long long> reg;
    Monad(vector<string> _pgm, int *input, size_t size);
    void run();
    void reset();
    long long get_reg(char a) { return reg[a]; };
};

#endif
