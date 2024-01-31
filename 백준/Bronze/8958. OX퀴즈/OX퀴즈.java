import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        String[] ls = new String[num];

        for(int i=0; i<ls.length; i++) {
            ls[i] = sc.next();
        }

        for(int i=0; i<num; i++) {
            int ans = 0;
            int answer = 0;
            for(int j=0; j<ls[i].length(); j++) {
                if(ls[i].charAt(j) == 'O') {
                    ans += 1;
                    answer += ans;
                } else {
                    ans = 0;
                }

            }
            System.out.println(answer);
        }
    }
}