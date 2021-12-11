#include <fstream>
#include <iostream>
#include <map>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    // initialize the maps and sets
    map<char,int> points;
    points[')'] = 3;
    points[']'] = 57;
    points['}'] = 1197;
    points['>'] = 25137;

    map<char,char> match;
    match['('] = ')';
    match[')'] = '(';
    match['['] = ']';
    match[']'] = '[';
    match['{'] = '}';
    match['}'] = '{';
    match['<'] = '>';
    match['>'] = '<';

    map<char,int> autocomplete_points;
    autocomplete_points[')'] = 1;
    autocomplete_points[']'] = 2;
    autocomplete_points['}'] = 3;
    autocomplete_points['>'] = 4;

    const string fname = argv[1];

    // parse the input file
    ifstream infile(fname);
    if (!infile) {
        perror(fname.c_str());
        exit(1);
    }

    string line;
    int error_score = 0;
    vector<unsigned long long> autocomplete_scores;
    while (infile >> line) {
        stack<char> stk;
        bool incomplete = true;
        for (char c : line) {
            if (autocomplete_points.find(c) != autocomplete_points.end()) {
                if (stk.empty() || stk.top() != match[c]) {
                    error_score += points[c];
                    incomplete = false;
                    break;
                } else {
                    stk.pop();
                }
            } else {
                stk.push(c);
            }
        }
        if (incomplete) {
            unsigned long long score = 0;
            while (!stk.empty()) {
                score = 5 * score + autocomplete_points[match[stk.top()]];
                stk.pop();
            }
            autocomplete_scores.push_back(score);
        }
    }

    cout << "Part 1: " << error_score << endl;
    sort(autocomplete_scores.begin(), autocomplete_scores.end());
    cout << "Part 2: " << autocomplete_scores[autocomplete_scores.size()/2] << endl;
}
