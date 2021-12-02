#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int num_larger(vector<int> &a) {
    int cnt = 0;
    for (size_t i = 1; i < a.size(); i++)
        if (a[i] > a[i-1])
            cnt++;
    return cnt;
}

int main(int argc, char *argv[]) {
    const string fname = argv[1];

    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(1);
    }

    vector<int> depth;
    int d;
    while (infile >> d)
        depth.push_back(d);
    
    cout << "Part 1: " << num_larger(depth) << endl;

    // compute sliding windows
    vector<int> windows;
    for (size_t i = 0; i < depth.size() - 2; i++)
        windows.push_back(depth[i] + depth[i+1] + depth[i+2]);
    cout << "Part 2: " << num_larger(windows) << endl;
}
