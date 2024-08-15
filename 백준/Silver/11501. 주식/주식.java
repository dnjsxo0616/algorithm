import java.util.*;

public class Main {
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int line = sc.nextInt();

      for(int i=0; i<line; i++) {
          int day = sc.nextInt();
          List<Integer> numbers = new ArrayList<>();

          for(int j=0; j<day; j++) {
              numbers.add(sc.nextInt());
          }

          long res = 0;
          int maxNum = numbers.get(numbers.size()-1);

          for(int k=numbers.size()-2; k>=0; k--) {
              int todayNum = numbers.get(k);
              if(maxNum >= todayNum) {
                  res += maxNum - todayNum;
              } else {
                  maxNum = todayNum;
              }
          }

          System.out.println(res);
      }
  }
}