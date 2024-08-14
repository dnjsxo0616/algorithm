
import java.util.*;

public class Main {
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int line = sc.nextInt();

      List<Integer> numbers = new ArrayList<>();
      int count = 0;

      for(int i=0; i<line; i++) {
          numbers.add(sc.nextInt());
      }

      for(int i=line-2; i>=0; i--) {
          int first = numbers.get(i);
          int second = numbers.get(i + 1);
          if(first >= second) {
              int c = (first - second) + 1;
              count += c;
              numbers.set(i, first-c);
          }
      }

      System.out.print(count);
  }
}