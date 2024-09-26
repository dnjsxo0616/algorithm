import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());

        long[] fibo = new long[91];
        fibo[1] = 1;


        for(int i=2; i<=num; i++) {
            fibo[i] = fibo[i-1] + fibo[i-2];
        }

        System.out.println(fibo[num]);
    }
}