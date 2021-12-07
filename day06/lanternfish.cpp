#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <vector>
#include <numeric>

using namespace std;

int main(int argc, char *argv[]) {
    // initialize the buckets
    vector<unsigned long long> fish(9, 0);

    // parse the input
    const char *fname = argv[1];
    FILE *fp;
    if ((fp = fopen(fname, "r")) == NULL) {
        perror(fname);
        exit(1);
    }
    int c;
    while ((c = fgetc(fp)) != EOF)
        if (isdigit(c))
            fish[c - '0']++;
    fclose(fp);

    // now run the generations;
    for (int day = 1; day <= 256; day++) {
        vector<unsigned long long> tmp(fish.begin()+1, fish.end());
        tmp[6] += fish[0];
        tmp.push_back(fish[0]);
        fish = tmp;

        if (day == 80)
            printf("Part 1: %llu\n", accumulate(fish.begin(), fish.end(), 0LL));
        else if (day == 256)
            printf("Part 2: %llu\n", accumulate(fish.begin(), fish.end(), 0LL));
    }
}
