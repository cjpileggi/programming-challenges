#ifndef ONLINE_JUDGE
    #define ONLINE_JUDGE false
#endif

#include <map>

using std::map;

unsigned int cycleLength(unsigned int n, map<int, int> maxMem)
{
    if (maxMem.find(n) != maxMem.end()) {
        return maxMem[n];
	}
    else
	{
        unsigned int orig = n, cnt = 1;
    
        while (n != 1) {
            cnt++;
            if (n%2 == 1) {n = 3*n+1;}
            else {n = n/2;}
		}
        maxMem[orig] = cnt;
        return cnt;
	}
}


unsigned int maxCycle(unsigned int i, unsigned int j, map<int, int> maxMem) {
    if (i > j)
	{
		unsigned int temp;
		temp = i;
		i = j;
		j = temp;
	}
	
	unsigned int maxCnt = 0;
	
	for (unsigned int c = i; c <= j; c++)
	{
		unsigned int curCycle = cycleLength(c, maxMem);
		if (curCycle >  maxCnt)
		{
			maxCnt = curCycle;
		}
	}
	
	return maxCnt;
}

int main()
{	
	unsigned int i, j;
	map<int, int> maxMem;
	
	//FILE *in = fopen("./text.txt", "r");
	//while(fscanf(in, "%d %d", &i, &j) != EOF ) {
	while(scanf("%d %d", &i, &j) != EOF ) {
		
		printf("%d %d %d\n", i, j, maxCycle(i, j, maxMem)); 
	}
    return 0;
}
