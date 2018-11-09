#try classes

from sys import stdin

from pandas import DataFrame


class Image:
    
    def __init__(self):
        self.img = []
        
    def newImgI(self, cmd):
        #return [["0"] * int(cmd[1])] * int(cmd[2]) creates duplicates of same list(all elements in column affected)
        self.img = []
        for i in range(0,cmd[2]):
            self.img.append(["0" for x in range(0,cmd[1])])

  

"""  def myfunc(abc):
    print("Hello my name is " + abc.name)


p1.myfunc()


p1.age = 40

#del p1.age
print(p1.age)

p1.j = "ug"

print(p1.j)

del p1"""


    
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
    
   

def fillF(img, cmd):
    
    maxX = len(img[0])
    maxY = len(img)
    
    origX = cmd[1]
    origY = cmd[2]
    
    newColor = cmd[3]
    oldColor = img[origY][origX]
    
    queueCur = 0
    
    
    queue = []
    visited = set()
    
    #img[origY][origX] = newColor
    queue.append((origX,origY))
    visited.add((origX,origY))
    
    nextX = 0
    nextY = 0
    
    img[queue[queueCur][1]][queue[queueCur][0]] = newColor
    if (queue[queueCur][0], queue[queueCur][1]) not in visited: 
        visited.add((queue[queueCur][0], queue[queueCur][1]))
 

    if (queue[queueCur][0], queue[queueCur][1]) not in visited: 
        visited.add((queue[queueCur][0], queue[queueCur][1]))
 
    while queueCur < len(queue):
        for i in range(-1,2):
            for j in range(-1,2):
                    nextX = queue[queueCur][0] + j
                    nextY = queue[queueCur][1] + i
                    
                    if nextX in range(0, maxX) and nextY in range(0,maxY):
                        if img[nextY][nextX] == oldColor:
                            img[nextY][nextX] = newColor
                            if (nextX,nextY) not in visited:
                                queue.append((nextX,nextY))
        queueCur += 1
    print(DataFrame(img))
    print("Queue",queue)
    print("Visit", visited)
    
    return img


def saveS(img,fName):
    print(fName)
    
    for x in img:
        for y in x:
            print(y, end="")
        print("")
    
if __name__ == "__main__":
    """img = []
    with open('pc165_inputs.txt') as f:
        for line in f: #stdin:#f: 
            #cmd = [x for x in line.split()]
            #print(cmd)
            if cmd[0] == "I": 
                img = newImgI(cmd)
                print(img)
            if cmd[0] == "C":
                img = clearC(img)
                print(img)
            if cmd[0] == "L":
                img = locationL(img,cmd)
                print(img)"""
            
      
    img = Image()
    
    
    img.newImgI([0,5,6])
    print(DataFrame(img.img), "\n")

    """img = locationL(img, [0, 2, 4, "F"])
    print(DataFrame(img), "\n")
            
                
    img = locationL(img, [0, 5, 3, "y"])
    print(DataFrame(img), "\n")
    
    img = clearC(img)
    print(DataFrame(img), "\n")
    
    img = vertV(img,[0,4,2,4,"B"])
    print(DataFrame(img), "\n")
    
    img = horizH(img,[0,3,2,4,"J"])
    print(DataFrame(img), "\n")
    
    img = newImgI([0,20,20])
    print(DataFrame(img), "\n")
    
    img = rectK(img,[0,3,3,6,6,"V"])
    print(DataFrame(img), "\n")"""
    
    """img = fillF(img, [0,4,4,"W"])
    print(DataFrame(img), "\n")"""
    
    """img = fillF(img, [0,6,3,"Q"])
    print(DataFrame(img), "\n")
    
    saveS(img,"k.bng")"""
    
    
    
    
            
        
        
