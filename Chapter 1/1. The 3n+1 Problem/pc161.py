"""
The 3n + 1 Problem

Programming Challenges (Skiena & Revilla): 1.6.1 The 3n + 1 Problem


UVa Online Judge: 100 The 3n + 1 Problem 
Judge Version: PYTH3 3.5.1 - Python 3

Best Time: 1.360 Seconds

"""

import sys
#import functools

#Caching can substitute the maxMem dictionary
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
        orig = n
        cnt = 1
    
        while n != 1:
            cnt += 1
            if n%2 ==1:
                n = 3*n+1
            else:
                n = n//2
        maxMem[orig] = cnt
        return cnt

#@functools.lru_cache(None)
def maxCycle(num1, num2, maxMem):
    """
        Calculates the maximum cycle between the given range 
    
        Calls the cycleLength function for each number 
    
        Parameters
        ----------
        num1 : int
            First number in range
        num2 : int
            Second number in range
        maxMem : dict
            Maximum Cycle-Length cache passed by reference
            
        Returns
        -------
        int
            maximum cycle in the range
    
    """
    # The judge may provide a set of numbers that are not in numerical order
    num1, num2 = min(num1, num2), max(num1, num2)
    return max(cycleLength(n, maxMem) for n in range(num1, num2+1))

if __name__ == '__main__':
    # Dictionary used to cache results of previously calculated cycle lengths
    # Key: integer n
    # Value: cycle-length for integer n
    maxMem = {}
    for line in sys.stdin:
        #Split input line into two integers: the beginning and end of the range
        num1, num2 = map(int, line.split()[:2])
        print(num1, num2, maxCycle(num1, num2, maxMem))
    exit(0)
    
"""
Minimized

import sys
def cycleLength(n,maxMem):
    if n in maxMem:return maxMem[n]
    else:
        orig,cnt=n,1
        while n != 1:
            cnt+=1
            if n%2==1:n=3*n+1
            else:n=n//2
        maxMem[orig]=cnt
        return cnt
def maxCycle(num1,end,maxMem):
    num1,end = min(num1,end), max(num1,end)
    return max(cycleLength(n,maxMem) for n in range(num1,end+1))
if __name__=='__main__':
    maxMem={}
    for line in sys.stdin:
        num1,num2 = map(int,line.split()[:2])
        print(num1,num2,maxCycle(num1,num2,maxMem))
    exit(0)

"""