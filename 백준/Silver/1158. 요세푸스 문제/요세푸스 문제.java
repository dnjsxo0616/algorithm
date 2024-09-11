import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        LinkedList<Integer> link = new LinkedList<>();
        for(int i=1; i<=n; i++) {
            link.add(i);
        }

        int index = 0;
        List<Integer> ans = new ArrayList<>();
        while(!link.isEmpty()) {
            index = (index + (k - 1)) % link.size();
            int r = link.remove(index);
            ans.add(r);
        }

        System.out.print("<");
        for(int i=0; i<n; i++) {
            System.out.print(ans.get(i));
            if(i < n-1) {
                System.out.print(", ");
            }
        }
        System.out.print(">");
    }
}