from sys import stdin
def mapLCD(s,n):
    for num in n:
        print(num)
    



if __name__ == "__main__":
    with open('pc164_inputs.txt') as f:
        for line in f: 
            s, n = map(str, line.split())
            print(mapLCD(s,n))
            