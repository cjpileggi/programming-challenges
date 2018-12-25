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
    		switch (cmd[0]) {
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
    				horizH();
    				break;
    			case 'K':
    				rectK();
    				break;
    			case 'F':
    				fillF();
    				break;
    			case 'S':
    				saveS();
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
