import java.util.Arrays;

class Solution {
    public int solution(int[] num_list, int n) {
        int answer = 0;
        boolean result = Arrays.stream(num_list)
            .anyMatch(i -> i == n);
        if(result) {
            answer = 1;
        }
        return answer;
    }
}