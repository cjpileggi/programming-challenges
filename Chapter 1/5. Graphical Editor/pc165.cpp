#ifndef ONLINE_JUDGE
    #define ONLINE_JUDGE false
#endif

class image {

	void command(char[] cmd)
	{
		switch (cmd[0]) {
			case "I": 
				newImgI();
				break;
			case "C":
				clearC();
				break;
			case "L":
				locationL();
				break;
			case "V":
				vertV();
				break;
			case "H":
				horizH();
				break;
			case "K":
				rectK();
				break;
			case "F":
				fillF();
				break;
			case "S":
				saveS();
				break;
			default:
				break;
		}
	}
};

int main()
{	

	//FILE *in = fopen("./text.txt", "r");
	//while(fscanf(in, "%d %d", &i, &j) != EOF ) {
	while(scanf("%d %d", &i, &j) != EOF ) {
		
		printf("%d %d %d\n", i, j, maxCycle(i, j, maxMem)); 
	} 


    return 0;
}