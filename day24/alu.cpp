#include <stdio.h>
#include <ctype.h>
#include <iostream>
#include <string>
#include "Odometer.h"

using namespace std;

const int LEN = 2;

// bool is_numeric(const string str) {
//     for (char c : str) {
//         if (!(isdigit(c) || c == '-'))
//             return false;
//     }
//     return true;
// }

int main(int argc, char *argv[]) {
    Odometer odometer(LEN);
    const int *digit;
    while ((digit = odometer.next()) != NULL) {
        for (int i = 0; i < LEN; i++) {
            cout << digit[i] << " ";
        }
        cout << endl;
    }

    // cout << "123 " << is_numeric("123") << endl;
    // cout << "1a23 " << is_numeric("1a23") << endl;
    // cout << "-123 " << is_numeric("-123") << endl;
}

    // for (int i01 = 1; i01 <= 9; i01++)
    // for (int i02 = 1; i02 <= 9; i02++)
    // for (int i03 = 1; i03 <= 9; i03++)
    // for (int i04 = 1; i04 <= 9; i04++)
    // for (int i05 = 1; i05 <= 9; i05++)
    // for (int i06 = 1; i06 <= 9; i06++)
    // for (int i07 = 1; i07 <= 9; i07++)
    // for (int i08 = 1; i08 <= 9; i08++)
    // for (int i09 = 1; i09 <= 9; i09++)
    // for (int i10 = 1; i10 <= 9; i10++)
    // for (int i11 = 1; i11 <= 9; i11++)
    // for (int i12 = 1; i12 <= 9; i12++)
    // for (int i13 = 1; i13 <= 9; i13++)
    // for (int i14 = 1; i14 <= 9; i14++) {
    //     cout << i01 << i02 << i03 << i04 << i05 << i06 << i07 << i08 << i09 << i10 << i11 << i12 << i13 << i14 << endl;
    // }
// }

     
