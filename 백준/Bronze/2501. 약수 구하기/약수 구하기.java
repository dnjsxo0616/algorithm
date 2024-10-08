import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int cont = 0;
        int ans = 0;

        for(int i = 1; i <= n; i++) {
            if(n % i == 0) {
                cont++;
            }
            if(cont == k) {
                ans = i;
                break;
            }
        }
        System.out.print(ans);
    }
}