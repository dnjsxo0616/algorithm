
import java.util.Map;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Map<String, Integer> map = Map.of(
        "black", 0,
        "brown", 1,
        "red", 2,
        "orange", 3,
        "yellow", 4,
        "green", 5,
        "blue", 6,
        "violet", 7,
        "grey", 8,
        "white", 9
    );

    Scanner sc = new Scanner(System.in);
    String x = sc.nextLine();
    String y = sc.nextLine();
    String z = sc.nextLine();

    int q = map.get(x);
    int w = map.get(y);
    int e = map.get(z);

    long qw = Long.parseLong(q + "" + w);
    long ee = (long) Math.pow(10, e);

    System.out.print(qw * ee);
  }
}