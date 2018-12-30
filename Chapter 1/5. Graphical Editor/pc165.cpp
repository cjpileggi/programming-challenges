#ifndef ONLINE_JUDGE
  #define ONLINE_JUDGE false
#endif

#include <string>
#include <algorithm>

using std::string;
using std::min;
using std::max;

class Image {

  public:
    char **img;
    int rows, cols;

    void command(char* cmd)
    {
      switch (cmd[0])
      {
        case 'I':
          newImgI(cmd[1], cmd[2]);
          break;
        case 'C':
          clearC();
          break;
        case 'L':
          locationL(cmd[1], cmd[2], cmd[3]);
          break;
        case 'V':
          vertV(cmd[1], cmd[2], cmd[3], cmd[4]);
          break;
        case 'H':
          horizH(cmd[1], cmd[2], cmd[3], cmd[4]);
          break;
        case 'K':
          rectK(cmd[1], cmd[2], cmd[3], cmd[4], cmd[5]);
          break;
        case 'F':
          fillF(cmd[1], cmd[2], cmd[3]);
          break;
        case 'S':
          saveS(cmd[1]);
          break;
        default:
          break;
      }
    }

    void newImgI(unsigned int M, unsigned int N)
    {
      //return [["0"] * int(cmd[1])] * int(cmd[2])
      //creates duplicates of same list(all elements in column affected)

      img = new char*[M];
      for(int i = 0; i < M; i++)
      {
        img[i] = new char[N];
        //self.img.append(["O" for x in range(0,M)])
      }

      for(int i=0; i < M; i++)
      {
        for(int j=0; j < N; j++)
        {
          img[i][j] = '0';
        }
      }
    }

    void clearC()
    {
      for(int i=0; i < rows; i++)
      {
        for(int j=0; j < cols; j++)
        {
          img[i][j] = '0';
        }
      }
    }

    void locationL(unsigned int X, unsigned int Y, char C)
    {
      img[Y - 1][X - 1] = C;
    }

    void vertV(unsigned int X, unsigned int Y1, unsigned int Y2, char C)
    {
      for(int y=(min(Y2,Y1) - 1 ); y < max(Y1,Y2); y++)
      {
        img[y][X-1] = C;
      }
    }

    void horizH(unsigned int X1, unsigned int X2, unsigned int Y, char C)
    {
      unsigned int lower = min(X2,X1) - 1;
      unsigned int upper = max(X1,X2) - 1;

      /*for x in range(lower, upper + 1):

      self.img[Y-1][x] = C #* (upper + 1) - lower)*/

      for (int i = lower; i <= upper; i++)
      {
        img[Y-1][i] = C;
      }
    }

    void rectK(unsigned int X1, unsigned int Y1, unsigned int X2, unsigned int Y2, char C)
    {

      unsigned int lower = min(X1,X2) - 1;
      unsigned int upper = max(X2,X1) - 1;

      for(int i = min(Y1,Y2) - 1; i <= max(Y2,Y1); i++)
      {
        for(int j = lower; j <= upper + 1; j++)
        {
          img[i][j] = C;
        }
      }
    }

    void fillF(unsigned int X, unsigned int Y, char C)
    {

      int maxX = sizeof(img[0]);
      int maxY = sizeof(img);

      int origX = X - 1;
      int origY = Y - 1;

      char oldColor = img[origY][origX];


      /*if(oldColor != C)
      {
        int queueCur = 0;

        /*queue = []
        visited = set()

        //img[origY][origX] = newColor
        queue.append((origX,origY))
        visited.add((origX,origY))

        nextX = 0
        nextY = 0

        self.img[queue[queueCur][1]][queue[queueCur][0]] = C
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
        if self.img[nextY][nextX] == oldColor:
        self.img[nextY][nextX] = C
        if (nextX,nextY) not in visited:
        queue.append((nextX,nextY))
        queueCur += 1
      }*/
    }

    void saveS(char Name)
    {
      printf("%s", Name);

      for(int i = 0; i < sizeof(img); i++)
      {
        for(int j = 0; j < sizeof(img[i]); j++)
        {
          printf("%c", j);
        }
        printf("\n");
      }
    }
};


int main()
{
  /*
  //FILE *in = fopen("./text.txt", "r");
  //while(fscanf(in, "%d %d", &i, &j) != EOF ) {
  while(scanf("%d %d", &i, &j) != EOF ) {

  printf("%d %d %d\n", i, j, maxCycle(i, j, maxMem));
  }

  */
  return 0;
}
