#include <fstream>
#include <iostream>
#include <string>
#include <regex>

using namespace std;

const bool hit_target(const int x1, const int x2, const int y1, const int y2, const int vix, const int viy) {
    int x = 0;
    int vx = vix;
    int y = 0;
    int vy = viy;

    while (1) {
        x += vx;
        if (--vx < 0)
            vx = 0;
        y += vy--;
        if (x1 <= x && x <= x2 && y1 <= y && y <= y2)
            return true;
        else if (x > x2 || y < y1)
            return false;
    }
}

int main(int argc, char *argv[]) {
    const string fname = argv[1];

    // parse the input file
    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(1);
    }

    int x1 = 0;
    int x2 = 0;
    int y1 = 0;
    int y2 = 0;
    string line;
    smatch m;
    regex e ("x=([\\d\\-]+)\\.\\.([\\d\\-]+), y=([\\d\\-]+)\\.\\.([\\d\\-]+)");
    while (getline(infile, line)) {
        regex_search(line, m, e);
        x1 = stoi(m[1]);
        x2 = stoi(m[2]);
        y1 = stoi(m[3]);
        y2 = stoi(m[4]);
    }

    // part 1
    int best_ymax = -1000000;
    for (int viy = 0; viy <= 1000; viy++) {
        int v = viy;
        int y = 0;
        int ymax = 0;
        while (1) {
            y += v;
            if (ymax < y)
                ymax = y;
            if (y1 <= y && y <= y2) {
                if (best_ymax < ymax)
                    best_ymax = ymax;
                break;
            } else if (y < y1)
                break;
            else
                v--;
        }
    }
    cout << "Part 1: " << best_ymax << endl;
                                    
    // part 2
    int cnt = 0;
    for (int vix = 0; vix <= x2; vix++)
        for (int viy = y1; viy <= 500; viy++)
            if (hit_target(x1, x2, y1, y2, vix, viy))
                cnt++;
    cout << "Part 2: " << cnt << endl;
}
