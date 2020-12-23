#include <stdio.h>

struct tuple find_pair(int q, int arr[]);

int find_triplet(int r, int ar[]);

struct tuple {
    int x1;
    int x2;
};


int main() {
    int a = 2020;
    int arr[200];
    int i;
    FILE *file;
    file = fopen("day1input.txt", "r");
    for (i = 0; i < 200; i++) { 
        fscanf(file, "%d", &arr[i]);
    };
    find_triplet(a, arr);
    return 0;
};

struct tuple find_pair(int q, int arr[]) {
    int i;
    int j;
    int n = 200;
    struct tuple ret;

    for (i=0; i < n; i++) {
        for (j=0; j < n; j++) {
           if (arr[j] == (q-arr[i])) {
               ret.x1 = arr[i];
               ret.x2 = arr[j];
           };
        };
    };
    return ret;
};

int find_triplet(int r, int ar[]) { 
    int i;
    int n = 200;
    int subsum;
    int mult;
    struct tuple ret;

    for (i=0; i < n; i++) { 
        subsum = r-ar[i];
        ret = find_pair(subsum, ar);
        if (ret.x1 + ret.x2 + ar[i] == r) { 
            mult = ret.x1 * ret.x2 * ar[i];
            printf("%d\n", mult);
        };
    };
    return 0;
};
