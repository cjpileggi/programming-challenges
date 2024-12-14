import java.util.Scanner;
import java.util.HashMap;
//import java.io.IOException;
//import java.io.BufferedReader;
//import java.io.FileReader;

public class Main { 
    
    private static int cycleLength(int n, HashMap<Integer, Integer> maxMem) {

        // If the cycle-length of current value seq was previously calculated and stored in maxMem,
       // retrieve seq's cycle length in maxMem, add it to cnt and exit the while loop
       if (maxMem.containsKey(n)) {
           return maxMem.get(n);
       }
       //cnt = maxMem.get(seq) + (cnt - 1);
       else {
           int seq = n, cnt = 1;
           while (seq != 1) {
               cnt++;
               if (seq % 2 == 1) {
                   seq = 3 * seq + 1;
               } else {
                   Math.floor(seq /= 2);
               }
           }
           maxMem.put(n, cnt);
           return cnt;
       }
       
   }

   private static int maxCycle(int i, int j, HashMap<Integer, Integer> maxMem) {
    // The judge might pass a pair of integers where the first is greater than the second
    // Swap the values if that is the case
    int x = Math.min(i, j);
    int y = Math.max(i, j);
    int curCycle = 0;
    int maxCnt = 0;

    // Loop through all integers between i and j find the integer with the greatest cycle-length
    for (int n = x; n <= y; n++) {
        curCycle = 0;

        if (maxMem.containsKey(n)) {
            curCycle = maxMem.get(n);
        }
        else {
            curCycle = cycleLength(n, maxMem);
        }

        maxCnt = Math.max(maxCnt, curCycle);
    }
    return maxCnt;
    }

    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        HashMap<Integer, Integer> maxMem = new HashMap<>();
        while (cin.hasNextInt()) {          
            int i = cin.nextInt();
            int j = cin.nextInt();
            System.out.println(i + " " + j + " " + maxCycle(i, j, maxMem));
        }
        cin.close();


        /*try (BufferedReader br = new BufferedReader(new FileReader("./p100.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                
                String[] numbers = line.split(" ");
                i = Integer.parseInt(numbers[0]);
                j = Integer.parseInt(numbers[1]);
                System.out.printf("%d %d %d%n", i, j, maxCycle(i, j, maxMem));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        scanner.close();*/
    }
}