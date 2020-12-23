#include <stdio.h>

int find_pair(int q, int arr[]);

int main() {
    int a = 2020;
    int arr[200];
    int i;
    FILE *file;
    file = fopen("day1input.txt", "r");
    for (i = 0; i < 200; i++) { 
        fscanf(file, "%d", &arr[i]);
    };
    find_pair(a, arr);
    return 0;
};

int find_pair(int q, int arr[]) {
    int i;
    int j;
    int mult;
    int n = 200;

    for (i=0; i < n; i++) {
        for (j=i; j < n; j++) {
           if (arr[j] == (q-arr[i])) {
               mult = arr[j] * arr[i];
               printf("%d", mult);
           };
        };
    };
    return 0;
};
