import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        return DFS(numbers, 0, target, 0);
    }
    public int DFS(int[] numbers, int depth, int target, int res) {
        if(depth == numbers.length) {
            return res == target ? 1 : 0;
        }
        
        int plus = res + numbers[depth];
        int minus = res - numbers[depth];
        
        return DFS(numbers, depth+1, target, plus) + DFS(numbers, depth+1, target, minus);
    }
}
