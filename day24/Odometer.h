#ifndef ODOMETER_H
#define ODOMETER_H

#include <cstddef>
#include <ostream>

using namespace std;

class Odometer {
private:
    size_t _len;
    int *_digit;
    bool _first;

public:
    Odometer(const size_t len);
    ~Odometer() { delete[] _digit; }
    size_t size() { return _len; }
    int digit(size_t i) { return _digit[i]; }
    int *next();
    void set_digits(const char *s);
};

#endif
