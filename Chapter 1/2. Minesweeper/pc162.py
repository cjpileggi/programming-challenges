"""
1.6.2 Minesweeper

"""
"""  """
from sys import stdin
def makeGame(grid,rows,cols):
    for i in range(0,rows):
        for j in range(0,cols):
            if grid[i][j] == "*":
                for x in range(max(0,i-1),min(i+2, rows)):
                    for y in range(max(0,j-1),min(j+2,  cols)):
                        if((x != i or y != j) and grid[x][y] != "*"):
                            if(grid[x][y] == "."): grid[x][y] = "1"
                            else: grid[x][y] = str(int(grid[x][y]) + 1)
            elif grid[i][j] == ".": grid[i][j] = "0"
                           
if __name__ == "__main__":
    
    tog, rows,cols, rowRev, grid, game,k = True,0,0,0,[],1,False
    #with open('pc162_inputs.txt') as f:
    for line in stdin: 
        if tog:
            rows, cols = map(int, line.split()[:2])
            if rows == 0: break
            tog,rowRev, grid= False, rows,[]
            continue
        else:
            grid.append(list(line.replace("\n","")))
            rowRev -= 1
            if rowRev == 0:
                makeGame(grid,rows,cols)
                if k == False:
                    k = True
                else : print("")
                tog = True
                print("Field #" + str(game) + ":")
                game += 1
                for i in range(0, rows):
                     print(''.join(str(i) for i in grid[i]))
    exit(0)
    