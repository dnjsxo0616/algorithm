import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] nums = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for(int j=0; j<m; j++) {
            int num = Integer.parseInt(st.nextToken());
            if((binarySearch(nums, num)) >= 0) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }
    public static int binarySearch(int[] nums, int key) {
        int lo = 0;
        int hi = nums.length - 1;

        while(lo <= hi) {
            int mid = (lo + hi) / 2;

            if (key < nums[mid]) {
                hi = mid - 1;
            } else if (key > nums[mid]) {
                lo = mid + 1;
            }
            else {
                return mid;
            }
        }
        return -1;
    }
}