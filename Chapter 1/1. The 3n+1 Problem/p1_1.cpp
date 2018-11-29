#ifndef ONLINE_JUDGE
    #define ONLINE_JUDGE false
#endif

#include <unordered_map>
#include <iostream>


using std::unordered_map;

unsigned int cycleLength(unsigned int n, unordered_map<int, int> &maxMem)
{
	unsigned int orig = n, cnt = 1;

	while (n != 1) {
		cnt++;
		if (n%2 == 1) {n = 3*n+1;}
		else {n /= 2;}
		
		if (maxMem.find(n) != maxMem.end())
		{
			cnt = maxMem[n] + (cnt - 1);
			break;
		}
	}
	maxMem[orig] = cnt;
	
	return cnt;
}


unsigned int maxCycle(unsigned int i, unsigned int j, unordered_map<int, int> &maxMem) {
    if (i > j)
	{
		unsigned int temp;
		temp = i;
		i = j;
		j = temp;
	}
	
	unsigned int maxCnt = 0, curCycle;
	for (unsigned int c = i; c <= j; c++)
	{
		curCycle = 0;
		if (maxMem.find(c) != maxMem.end())
		{
			curCycle = maxMem[c];
		}
		else
		{
			curCycle = cycleLength(c, maxMem);
		}
		
		
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
	unordered_map<int, int> maxMem;
	
	//FILE *in = fopen("./text.txt", "r");
	//while(fscanf(in, "%d %d", &i, &j) != EOF ) {
	while(scanf("%d %d", &i, &j) != EOF ) {
		
		printf("%d %d %d\n", i, j, maxCycle(i, j, maxMem)); 
	} 
	// Create a map iterator and point to beginning of map
	/*std::map<int, int>::iterator it = maxMem.begin();
 
	// Iterate over the map using Iterator till end.
	while (it != maxMem.end())
	{
		// Accessing KEY from element pointed by it.
		int word = it->first;
 
		// Accessing VALUE from element pointed by it.
		int count = it->second;
 
		std::cout << word << " :: " << count << std::endl;
 
		// Increment the Iterator to point to next entry
		it++;
	} */
    return 0;
} 

/*
#ifndef ONLINE_JUDGE
    #define ONLINE_JUDGE false
#endif

#include <unordered_map>
//#include <iostream>


using std::unordered_map;

unsigned int cycleLength(unsigned int n, unordered_map<int, int> &maxMem)
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


unsigned int maxCycle(unsigned int i, unsigned int j, unordered_map<int, int> &maxMem) {
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
	unordered_map<int, int> maxMem;
	
	//FILE *in = fopen("./text.txt", "r");
	//while(fscanf(in, "%d %d", &i, &j) != EOF ) {
	while(scanf("%d %d", &i, &j) != EOF ) {
		
		printf("%d %d %d\n", i, j, maxCycle(i, j, maxMem)); 
	} 
	// Create a map iterator and point to beginning of map
	/*std::map<int, int>::iterator it = maxMem.begin();
 
	// Iterate over the map using Iterator till end.
	while (it != maxMem.end())
	{
		// Accessing KEY from element pointed by it.
		int word = it->first;
 
		// Accessing VALUE from element pointed by it.
		int count = it->second;
 
		std::cout << word << " :: " << count << std::endl;
 
		// Increment the Iterator to point to next entry
		it++;
	} 
    return 0;
}*/
