"""
The 3n + 1 Problem

Programming Challenges (Skiena & Revilla): 1.6.1 The 3n + 1 Problem

Online Judge: Problem 100 - The 3n + 1 Problem
Judge Version: PYTH3 3.5.1 - Python 3
Best Run Time: 1.360 Seconds

"""

import sys
#import functools

#Caching can substitute the maxMem dictionary for improving performance
#@functools.lru_cache(None)
def cycleLength(n, maxMem):
    """
        Calculates the cycle-legnth of a number

        Parameters
        ----------
        n : int
            integer to calculate cycle-length for
        maxMem : dict
            Maximum Cycle-Length cache passed by reference

        Returns
        -------
        int
            the cycle-length of the given interval

    """
    # Used the stored value in the cache if the was previously calculated
    if n in maxMem:
        return maxMem[n]
    else:
        seq = n
        cnt = 1

        while seq != 1:
            cnt += 1
            if seq % 2 ==1:
                seq = 3*seq + 1
            else:
                seq = seq // 2
        maxMem[n] = cnt
        return cnt

#@functools.lru_cache(None)
def maxCycle(i, j, maxMem):
    """
        Calculates the maximum cycle between the given range

        Calls the cycleLength function for each number

        Parameters
        ----------
        i : int
            First number in range
        j : int
            Second number in range
        maxMem : dict
            Maximum Cycle-Length cache passed by reference

        Returns
        -------
        int
            maximum cycle in the range

    """
    # The judge may provide a set of numbers that are not in ascending order
    # The lowest integer must always be first for the algorithm to work
    i, j, curCycle, maxCnt = min(i, j), max(i, j), 0, 0

    return max(cycleLength(n, maxMem) for n in range(i, j+1))

    # for-loop replaced with inline statement above
    """for n in range(i, j+1):
        curCycle = 0

        if n in maxMem:
            curCycle = maxMem[n]
        else:
            curCycle = cycleLength(n, maxMem)

        maxCnt = max(maxCnt, curCycle)
    return maxCnt"""

if __name__ == '__main__':
    # Dictionary used to cache results of previously calculated cycle lengths
    # Key: integer n
    # Value: cycle-length for integer n
    i, j, maxMem = 0, 0, {}
    for line in sys.stdin:
        #Split input line into two integers: the beginning and end of the range
        i, j = map(int, line.split()[:2])
        print(i, j, maxCycle(i, j, maxMem))

    # Read inputs from file used for testing
    """f = open("p100.txt", "r")
    for line in f:
        i, j = map(int, line.split()[:2])
        print(i, j, maxCycle(i, j, maxMem))"""
    exit(0)
