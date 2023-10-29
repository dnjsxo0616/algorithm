import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String words = "";
        
        for(int i=0; i<a.length(); i++) {
            char c = a.charAt(i);
            
            if(Character.isLowerCase(c)){
                words += Character.toUpperCase(c);
            } else {
                words += Character.toLowerCase(c);
            }
        }
        System.out.print(words);
    }
}