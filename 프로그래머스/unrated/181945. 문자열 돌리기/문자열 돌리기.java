import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String[] numbers = a.split("");
        for(int i=0; i<numbers.length; i++) {
            System.out.println(numbers[i]);
        }
    }
}