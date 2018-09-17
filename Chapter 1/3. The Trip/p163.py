
def minPrice(prices):
    minP = 0
    pricesAvg = sum(prices)/len(prices)
    for p in prices:
        if p < pricesAvg:
            #print(p - pricesAvg, float(format(pricesAvg - p, '.3f')[:-1]))
            minP += float(format(pricesAvg - p, '.3f')[:-1])
        
    return "${}".format(minP) 

def avg(lst):
    return sum(lst) / len(lst)


if __name__ == "__main__":
    flag, priceNum = True, 0
    with open('pc163_inputs.txt') as f:
        for line in f: #stdin: 
            if flag:
                priceNum = int(line)
                flag=False
            else:
                prices = [float(p) for p in line.split()]
                print(prices)
                priceNum -= 1
                if priceNum == 0:
                    flag = True
                print(minPrice(prices))
