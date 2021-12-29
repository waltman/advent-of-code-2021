#ifndef ODOMETER_H
#define ODOMETER_H

#include <cstddef>

using namespace std;

class Odometer {
private:
    size_t _len;
    int *_digit;
    bool _first;

public:
    Odometer(const size_t len);
    ~Odometer() { delete _digit; }
    const int *next();
};

#endif
