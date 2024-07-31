import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int c = nums.length / 2;
        int[] num = Arrays.stream(nums)
            .distinct()
            .toArray();
        int res = num.length;
        return c > res ? res : c;
    }
}