"""
1.6.1 The 3n + 1 Problem

"""
"""  """
def maxCycle(i,j):
    maxi = 0
    for x in range(i, j + 1):
        tot=0
        while(x > 1):
            if x % 2 == 0: x /= 2
            else: x = x * 3 + 1
            tot += 1
        if (tot > maxi): maxi = tot + 1
    return maxi

def pc1():
    with open('pc161_inputs.txt') as f:
       for line in f:
          lst = [int(y) for y in line.replace("\n","").split(' ')]
          print "{0} {1} {2}".format(lst[0], lst[1], maxCycle(lst[0],lst[1]))

if __name__ == "__main__": pc1()