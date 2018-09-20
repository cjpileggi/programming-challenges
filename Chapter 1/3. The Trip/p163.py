from sys import stdin
def minPrice(prices):
    minP, maxP = 0, 0
    pricesAvg = sum(prices)/len(prices)
    for p in prices:
        if p < pricesAvg:
            #print(p - pricesAvg, float(format(pricesAvg - p, '.3f')[:-1]))
            minP += float(format(pricesAvg - p, '.3f')[:-1])
        
        if p > pricesAvg:
            #print(p - pricesAvg, float(format(pricesAvg - p, '.3f')[:-1]))
            maxP += float(format(p - pricesAvg, '.3f')[:-1])
    
    return "${:.2f}".format(max(minP,maxP)) 


if __name__ == "__main__":
    flag, priceNum,prices = True, 0, []
    with open('pc163_inputs.txt') as f:
        for line in f: #stdin: 
            if flag:
                priceNum = int(line)
                flag=False
            else:
                prices.append(float(line.replace("\n","")))
                priceNum -= 1
                priceNum
                if priceNum == 0:
                    flag = True
                    print(minPrice(prices))
                    prices = []
