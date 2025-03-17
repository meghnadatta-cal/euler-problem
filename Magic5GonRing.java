import java.util.Arrays;
import java.util.Scanner;

public class Magic5GonRing {
    static String maxString = "0"; 

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numbers = new int[10];

        System.out.println("Enter 10 unique numbers (1-10) for the 5-gon ring:");
        for (int i = 0; i < 10; i++) {
            numbers[i] = scanner.nextInt();
        }
        scanner.close();

        Arrays.sort(numbers); 
        permute(numbers, 0);

        System.out.println("Maximum 16-digit string for the magic 5-gon ring: " + maxString);
    }

    
    static void permute(int[] arr, int index) {
        if (index == arr.length) {
            checkMagicGon(arr);
            return;
        }
        for (int i = index; i < arr.length; i++) {
            swap(arr, i, index);
            permute(arr, index + 1);
            swap(arr, i, index); 
        }
    }

    
    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }


    static void checkMagicGon(int[] arr) {
    
        int[][] lines = {
            { arr[5], arr[0], arr[1] },
            { arr[6], arr[1], arr[2] },
            { arr[7], arr[2], arr[3] },
            { arr[8], arr[3], arr[4] },
            { arr[9], arr[4], arr[0] }
        };

        int sum = lines[0][0] + lines[0][1] + lines[0][2];
        for (int i = 1; i < 5; i++) {
            if (lines[i][0] + lines[i][1] + lines[i][2] != sum) {
                return;
            }
        }

       
        int minIndex = 0;
        for (int i = 1; i < 5; i++) {
            if (lines[i][0] < lines[minIndex][0]) {
                minIndex = i;
            }
        }

        
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < 5; i++) {
            int index = (minIndex + i) % 5;
            result.append(lines[index][0]).append(lines[index][1]).append(lines[index][2]);
        }

        String resultString = result.toString();
        if (resultString.length() == 16 && resultString.compareTo(maxString) > 0) {
            maxString = resultString;
        }
    }
}
