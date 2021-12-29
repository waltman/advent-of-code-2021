#include <fstream>
#include <iostream>
#include <string>
#include "Monad.h"

using namespace std;

const string PGM = "test1.txt";

int main(int argc, char *argv[]) {
    ifstream infile(PGM);
    if (!infile) {
        perror(PGM.c_str());
        exit(1);
    }

    int inp[1];
    inp[0] = -2;
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
