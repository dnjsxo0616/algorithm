import java.util.Arrays;

class Solution {
    public int solution(int[] num_list) {
        int sum = Arrays.stream(num_list)
            .reduce(1, (a,b) -> a*b);
        
        System.out.println(sum);
        
        int times = Arrays.stream(num_list)
            .sum();
        
        int sum_square = (int) Math.pow(times, 2);
        
        return sum < sum_square ? 1 : 0;
    }
}