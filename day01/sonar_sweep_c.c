#include <stdio.h>
#include <stdlib.h>

const int MAX_LINES = 2000;

int num_larger(int *a, int len) {
    int cnt = 0;
    for (int i = 1; i < len; i++) {
        if (a[i] > a[i-1])
            cnt++;
    }
    return cnt;
}

int main(int argc, char *argv[]) {
    char *fname = argv[1];
    int depth[MAX_LINES];
    int depth_len = 0;
    FILE *fp;
    if ((fp = fopen(fname, "r")) == NULL) {
        perror(fname);
        exit(1);
    }
    char line[80];
    while (fgets(line, sizeof(line), fp))
        depth[depth_len++] = atoi(line);
    printf("Part 1: %d\n", num_larger(depth, depth_len));

    // compute sliding windows
    int windows[MAX_LINES];
    int window_len = 0;
    for (int i = 0; i < depth_len - 2; i++)
        windows[window_len++] = depth[i] + depth[i+1] + depth[i+2];
    printf("Part 2: %d\n", num_larger(windows, window_len));

}
