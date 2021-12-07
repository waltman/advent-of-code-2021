#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <numeric>

using namespace std;

int main(int argc, char *argv[]) {
    // initialize the buckets
    unsigned long long fish[9];
    memset(fish, 0, sizeof(fish));

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
        unsigned long long tmp[9];
        memcpy(tmp, fish+1, sizeof(unsigned long long) * 8);
        tmp[6] += fish[0];
        tmp[8] = fish[0];
        memcpy(fish, tmp, sizeof(fish));

        if (day == 80)
            printf("Part 1: %llu\n", accumulate(fish, fish+9, 0LL));
        else if (day == 256)
            printf("Part 2: %llu\n", accumulate(fish, fish+9, 0LL));
    }
}
