/*
  The 3n + 1 Problem

  Programming Challenges (Skiena & Revilla): 1.6.1 The 3n + 1 problem

	Online Judge: Problem 100 - The 3n + 1 problem
  Judge Version: C++ 5.3.0 - GNU C++ Compiler
	Best Runtime - 0.010s

  - Uses unsigned int throughout program since input is always 0 or greater
*/

#ifndef ONLINE_JUDGE
    #define ONLINE_JUDGE false
#endif

#include <unordered_map>
#include <iostream>

using std::unordered_map;

// Find the cycle-length of integer n according to the algorithm provided in the problem
unsigned int cycleLength(unsigned int n, unordered_map<int, int> &maxMem)
{
	// Loop to find the sequence of numbers starting with n and ending 1
	// Increment cnt by 1 for each iteration in the loop. The final number is the cycle cycleLength
	// Begin with 1 since 1 will always be the last integer in a sequence
	unsigned int seq = n, cnt = 1;
	while (seq != 1)
	{
		cnt++;
		if (seq % 2 == 1) { seq = 3*seq + 1; }
		else { seq /= 2; }

		// If the cycle-length of current value seq was previously calculated and stored in maxMem,
		// retrieve seq's cycle length in maxMem, add it to cnt and exit the while loop
		if (maxMem.find(seq) != maxMem.end())
		{
			cnt = maxMem[seq] + (cnt - 1);
			break;
		}
	}
	maxMem[n] = cnt;

	return cnt;
}

// Find the integer that exists between integers i and j with the greatest cycle-length
unsigned int maxCycle(unsigned int i, unsigned int j, unordered_map<int, int> &maxMem)
{
	// The judge might pass a pair of integers where the first is greater than the second
	// Swap the values if that is the case
	// The algorithm will run incorrectly if the first integer is greater than the second
	if (i > j)
	{
		unsigned int temp;
		temp = i;
		i = j;
		j = temp;
	}

	// Loop through all integers between i and j find the integer with the greatest cycle-length
	// maxCnt - integer with the greatest cycle-length in the loop
	// curCycle - cycle-length of integer evaluated in loop iteration
	unsigned int maxCnt = 0, curCycle;
	for (unsigned int n = i; n <= j; n++)
	{
		curCycle = 0;
		// If integer n was already evaluated and the cycle-length was stored in maxMem, use that value
		// Otherwise, calculate the cycle-lenth of n
		if (maxMem.find(n) != maxMem.end())
		{
			curCycle = maxMem[n];
		}
		else
		{
			curCycle = cycleLength(n, maxMem);
		}
		// Assign to maxCnt the greatest cycle-length in the for-loop
		if (curCycle >  maxCnt)
		{
			maxCnt = curCycle;
		}
	}
	return maxCnt;
}

int main()
{
	unsigned int i, j; // Two input integers
	// Unordered map used to store previously determined cycles
	// <integer, cycle length of integer>
	unordered_map<int, int> maxMem;

	// Read inputs from Online Judge
	while(scanf("%d %d", &i, &j) != EOF )
	{
		printf("%d %d %d\n", i, j, maxCycle(i, j, maxMem));
	}

	// Read inputs from file used for testing
	/*
	FILE *in = fopen("./p100.txt", "r");
	while(fscanf(in, "%d %d", &i, &j) != EOF )
	{
		printf("%d %d %d\n", i, j, maxCycle(i, j, maxMem));
	}
	*/
  return 0;
}
