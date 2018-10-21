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
"""    
def vertV():
    
def horizH():
    
def rectK():
    
def fillF():
    
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
    print(img)
    
    # img[0][3] = "h"
    print(img)  
    
    img = locationL(img, [0, 2, 4, "F"])
    print(img)
            
                
    img = locationL(img, [0, 5, 3, "y"])
    print(img)
            
        
        
