#include "Odometer.h"

Odometer::Odometer(const size_t len) {
    _first = true;
    _len = len;
    _digit = new int[_len];
    for (size_t i = 0; i < _len; i++)
        _digit[i] = 9;
}

const int *Odometer::next() {
    if (_first) {
        _first = false;
        return _digit;
    } else {    
        int i = _len-1;
        while (i >= 0) {
            if (--_digit[i] >= 1)
                return _digit;
            else {
                _digit[i] = 9;
                i--;
            }
        }
        return NULL;
    }
}
