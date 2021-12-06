#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include "array2d.h"

using namespace std;

struct Line {
    int x1;
    int y1;
    int x2;
    int y2;
};

const int num_overlaps(array2d<int> &grid) {
    int cnt = 0;
    for (int row = 0; row < grid.y_dim(); row++)
        for (int col = 0; col < grid.x_dim(); col++)
            if (grid(row, col) > 1)
                cnt++;
    return cnt;
}

int main(int argc, char *argv[]) {
    const string fname = argv[1];

    // parse the input file
    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(1);
    }

    int x1, y1, x2, y2;
    string line;
    smatch m;
    regex e ("(\\d+),(\\d+) -> (\\d+),(\\d+)");
    vector<struct Line> lines;
    while (getline(infile, line)) {
        regex_search(line, m, e);
        x1 = stoi(m[1]);
        y1 = stoi(m[2]);
        x2 = stoi(m[3]);
        y2 = stoi(m[4]);

        Line line = {x1, y1, x2, y2};
        lines.push_back(line);
    }
    infile.close();

    // make an empty grid
    const int DIM = 1000;
    array2d<int> grid(DIM, DIM, 0);

    // draw the horizontal and vertical lines
    for (auto line : lines) {
        if (line.x1 == line.x2) {
            const int delta = (line.y1 < line.y2) ? 1 : -1;
            for (int y = line.y1; y != line.y2 + delta; y += delta)
                grid(y,line.x1) += 1;
        } else if (line.y1 == line.y2) {
            int delta = (line.x1 < line.x2) ? 1 : -1;
            for (int x = line.x1; x != line.x2 + delta; x += delta)
                grid(line.y1,x) += 1;
        }
    }
    cout << "Part 1: " << num_overlaps(grid) << endl;

    // draw the diagonal lines
    for (auto line : lines) {
        if (line.x1 != line.x2 && line.y1 != line.y2) {
            const int dx = (line.x1 < line.x2) ? 1 : -1;
            const int dy = (line.y1 < line.y2) ? 1 : -1;
            int x, y;
            for (x = line.x1, y = line.y1; x != line.x2 + dx; x += dx, y += dy)
                grid(y,x) += 1;
        }
    }
    cout << "Part 2: " << num_overlaps(grid) << endl;
    
}
