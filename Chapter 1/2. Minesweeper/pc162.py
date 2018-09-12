"""
1.6.2 Minesweeper

"""
"""  """
def makeGame(grid,dims):
    newGrid,rowMax,colMax = [dims[0],dims[1]], dims[0],dims[1]
    
    for i in range(0,rowMax):
        for j in range(0,colMax):
            if grid[i][j] == "*":
                for x in range(max(0,i-1),min(i+2, rowMax)):
                    for y in range(max(0,j-1),min(j+2,  colMax)):
                        if((x != i or y != j) and grid[x][y] != "*"):
                            if(grid[x][y] == "."): grid[x][y] = "1"
                            else: grid[x][y] = str(int(grid[x][y]) + 1)
            elif grid[i][j] == ".": grid[i][j] = "0"
                
def pc162():
    tog, dim, rowRev, grid, game = True,[],0,[],1
    with open('pc162_inputs.txt') as f:
       for line in f: 
           if tog:
               dim = [int(y) for y in line.replace("\n","").split(' ')]
               if dim[0] == 0: break
               tog,rowRev, grid= False, dim[0],[] #del grid[:]
               continue
           else:
               grid.append(list(line.replace("\n","")))
               rowRev -= 1
               if rowRev == 0:
                   makeGame(grid,dim)
                   tog = True
                   print "Field #" + str(game) + ":"
                   game += 1
                   for i in range(0, dim[0]):
                        print ''.join(str(i) for i in grid[i])
                   print ""
               
                   

if __name__ == "__main__":
    
    pc162()