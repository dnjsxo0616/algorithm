
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    for(int i=0; i<a; i++) {

      int b = sc.nextInt();
      int c = sc.nextInt();

      int res = 1;

      for(int j=0; j<c; j++) {
        res = res * b%10;
      }

      res = res==0 ? 10 : res;

      System.out.println(res);
    }
  }
}