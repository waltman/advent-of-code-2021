#include <fstream>
#include <iostream>
#include <string>
#include "Monad.h"

using namespace std;

const string PGM = "test3.txt";

int main(int argc, char *argv[]) {
    ifstream infile(PGM);
    if (!infile) {
        perror(PGM.c_str());
        exit(1);
    }

    int inp[1];
    inp[0] = 10;
    Monad monad(inp);
    string line;
    while (getline(infile, line))
        monad.add_cmd(line);

    for (int i = 0; i < 16; i++) {
        inp[0] = i;
        monad.reset(inp);
        monad.run();
        cout << "i=" << i << " " << monad << endl;
    }
}
