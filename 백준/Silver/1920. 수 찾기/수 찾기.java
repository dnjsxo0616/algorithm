import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        m = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] nums = new int[m];
        for (int i = 0; i < m; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);

        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] finds = new int[n];
        for (int i = 0; i < n; i++) {
            int input = Integer.parseInt(st.nextToken());
            if(binarySearch(nums, input)) {
                System.out.println(1);
            }else System.out.println(0);
        }
    }

    public static boolean binarySearch(int[] nums, int key) {
        int lo = 0;
        int hi = nums.length-1;

        while (lo <= hi) {
            int mid = (lo + hi) / 2;

            if (key < nums[mid]) {
                hi = mid - 1;
            } else if (key > nums[mid]) {
                lo = mid + 1;
            } else {
                return true;
            }
        }
        return false;
    }
}