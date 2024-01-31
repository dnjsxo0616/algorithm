import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> numbers = new ArrayList<>();
        for(int i=0; i<8; i++) {
            numbers.add(sc.nextInt());
        }

        List<Integer> ref = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8);
        List<Integer> reversedRef = new ArrayList<>(ref);
        Collections.reverse(reversedRef);

        if (numbers.equals(ref)) {
            System.out.println("ascending");
        } else if (numbers.equals(reversedRef)) {
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }

    }
}