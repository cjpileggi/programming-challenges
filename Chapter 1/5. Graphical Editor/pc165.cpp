#ifndef ONLINE_JUDGE
    #define ONLINE_JUDGE false
#endif

#include <string>

using std::string;

class Image {

	public:
    unsigned int **img;

    void command(string[] cmd)
    	{
    		switch (cmd[0]) {
    			case 'I':
    				newImgI();
    				break;
    			case 'C':
    				clearC();
    				break;
    			case 'L':
    				locationL();
    				break;
    			case 'V':
    				vertV();
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
            img = new unsigned int*[N];
            for(int i = 0; i < N; i++)
            {
                img[i] = new unsigned int[M];
              //self.img.append(["O" for x in range(0,M)])
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
