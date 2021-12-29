#include <fstream>
#include <iostream>
#include <string>
#include "Monad.h"

using namespace std;

const string PGM = "test2.txt";

int main(int argc, char *argv[]) {
    ifstream infile(PGM);
    if (!infile) {
        perror(PGM.c_str());
        exit(1);
    }

    int inp[2];
    inp[0] = 3;
    inp[1] = 9;
    Monad monad(inp);
    string line;
    while (getline(infile, line))
        monad.add_cmd(line);

    cout << "before" << endl;
    cout << monad << endl;

    monad.run();
    cout << "after" << endl;
    cout << monad << endl;
}
