import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int ans = 1;
        int count = 6;
        int res = 1;
        if (n > 1) {
            while (res < n) {
                res += count;
                count += 6;
                ans++;
            }
        }
        System.out.println(ans);
    }
}