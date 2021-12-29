#include <stdio.h>
#include <ctype.h>
#include <iostream>
#include <fstream>
#include <string>
#include <time.h>
#include "Odometer.h"
#include "Monad.h"
#include "timer.h"

using namespace std;

const int LEN = 14;
const string PGM = "input1.txt";

void dump(int *digit) {
    for (int i = 0; i < LEN; i++) {
        cout << digit[i];
    }
    cout << endl;
}

void report(const Timer &timer, const char *s) {
    double stime = timer.stime();
    double utime = timer.utime();
    double ttime = stime + utime;
    double wtime = timer.wtime();

    printf("%12s: %10.6f clock, %10.6f sys, %10.6f user, %10.6f total\n",
           s, wtime, stime, utime, ttime);
}

int main(int argc, char *argv[]) {
    ifstream infile(PGM);
    if (!infile) {
        perror(PGM.c_str());
        exit(1);
    }

    Monad monad(NULL);
    string line;
    while (getline(infile, line))
        monad.add_cmd(line);

    Odometer odometer(LEN);
    if (argc > 1)
        odometer.set_digits(argv[1]);

    int *digit;
    unsigned long long step = 0;
    Timer compute;
    while ((digit = odometer.next()) != NULL) {
        if ((++step % 1000000000) == 0) {
            cout << "clock = " << time(NULL) << " step = " << step << " odometer = ";
            dump(digit);
        }
        monad.reset(digit);
        monad.run();
        // dump(digit);
        // cout << monad << endl;
        if (monad.get_reg('z') == 0) {
            cout << "Part 1: ";
            dump(digit);
            cout << monad << endl;
            break;
        }
    }
}
