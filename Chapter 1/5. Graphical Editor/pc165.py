#try classes

from sys import stdin

def newImgI(cmd):
    #return [["0"] * int(cmd[1])] * int(cmd[2]) creates duplicates of same list(all elements in column affected)
    img = []
    
    for i in range(0,cmd[2]):
        img.append(["0" for x in range(0,cmd[1])])
    return img
    
def clearC(img):
    return [["0" for x in img[0]] for x in img]

def locationL(img, cmd):
    img[(len(img)-int(cmd[2]))][int(cmd[1]) - 1] = cmd[3]
    return img

def vertV(img, cmd):
    for x in range(len(img)- int(cmd[3]),(len(img)- int(cmd[2])) + 1):
        img[x][cmd[3]] = cmd[4]
    return img    


def horizH(img, cmd):
    lower = int(cmd[2]) - 1
    upper = int(cmd[3])
    
    img[int(cmd[1]) + 1][lower:upper] = cmd[4] * (upper - lower)
    
    return img

def rectK(img, cmd):
    
    lower = int(cmd[1]) - 1
    upper = int(cmd[3])
    
    for y in range(len(img)- int(cmd[4]), (len(img)- int(cmd[2])) + 1):
    
        img[y][lower:upper] = cmd[5] * (upper - lower)
    
    return img
    
    
"""def fillF(img, cmd):
    
    maxX = len(img[0])
    maxY = len(img)
    
    pnt = [cmd[1],cmd[2]]
    pnts = []
    oldC = img[pnt[0] - 1][pnt[1] - 1]
    
    img[cmd[1] - 1][cmd[2] - 1] = cmd[3]
    
    if pnt[0] != 0:
"""       
    
    
"""  
def saveS():"""

if __name__ == "__main__":
    img = []
    with open('pc165_inputs.txt') as f:
        for line in f: #stdin:#f: 
            #cmd = [x for x in line.split()]
            #print(cmd)
            """if cmd[0] == "I": 
                img = newImgI(cmd)
                print(img)
            if cmd[0] == "C":
                img = clearC(img)
                print(img)
            if cmd[0] == "L":
                img = locationL(img,cmd)
                print(img)"""
            
      
    
    img = newImgI([0,5,6])
    print(img, "\n")

    img = locationL(img, [0, 2, 4, "F"])
    print(img, "\n")
            
                
    img = locationL(img, [0, 5, 3, "y"])
    print(img, "\n")
    
    img = clearC(img)
    print(img, '\n')
    
    img = vertV(img,[0,4,2,4,"B"])
    print(img, '\n')
    
    img = horizH(img,[0,3,2,4,"J"])
    print(img, '\n')
    
    img = newImgI([0,10,10])
    print(img, "\n")
    
    img = rectK(img,[0,3,3,6,6,"V"])
    print(img, "\n")
    
    """fillF(img, [0,3,3,"W"])
    print(img, "\n")"""
    
    
            
        
        
