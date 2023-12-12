#include <stdio.h>

int cycleSize(int x) {
    int cycle = 1;

    while (x != 1) {
        if (x % 2 == 0) {
            x = x / 2;
        } else {
            x = x * 3 + 1;
        }
        ++cycle;
    }
    return cycle;
}

int maxCycleSizeBetween(int a, int b) {
    if (a > b) {
        int temp = a;
        a = b;
        b = temp;
    }
    int maxCycle = 0;
    
    for (; a <= b; a++) {
        int thisCycleSize = cycleSize(a);
        if (thisCycleSize > maxCycle) {
            maxCycle = thisCycleSize;
        }
    }
    return maxCycle;
}

int main() {
    int a, b;
    
    while (scanf("%d %d", &a, &b) != EOF) {
        printf("%d %d %d\n", a, b, maxCycleSizeBetween(a, b));
    }


    return 0;
}

    /*
    FILE *in = fopen("./p100.txt", "r");
	while(fscanf(in, "%d %d", &a, &b) != EOF )
	{
        printf("%d %d %d\n", a, b, maxCycleSizeBetween(a, b));
	}
    */