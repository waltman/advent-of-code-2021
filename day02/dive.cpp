#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Cmd {
    string cmd;
    int val;
};

int main(int argc, char *argv[]) {
    const string fname = argv[1];

    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(1);
    }

    string cmd;
    int val;
    vector<struct Cmd> cmds;
    while (infile >> cmd >> val) {
        struct Cmd c = {cmd, val};
        cmds.push_back(c);
    }

    int d = 0;
    int h = 0;
    int a = 0;
    for (auto cmd : cmds)
        if (cmd.cmd == "forward")
            h += cmd.val;
        else if (cmd.cmd == "down")
            d += cmd.val;
        else if (cmd.cmd == "up")
            d -= cmd.val;
    cout << "Part 1: " << d * h << endl;

    d = 0; h = 0; a = 0;
    for (auto cmd : cmds)
        if (cmd.cmd == "forward") {
            h += cmd.val;
            d += a * cmd.val;
        } else if (cmd.cmd == "down")
            a += cmd.val;
        else if (cmd.cmd == "up")
            a -= cmd.val;
    cout << "Part 2: " << d * h << endl;
}
