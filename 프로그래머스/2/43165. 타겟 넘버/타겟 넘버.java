import java.util.*;

class Solution {
    int count = 0;
    public int solution(int[] numbers, int target) {
        int answer = 0;
        DFS(numbers, 0, target, 0);
        return answer = count;
    }
    
    public void DFS(int[] numbers, int depth, int target, int result) {
        if(depth == numbers.length) {
            if(result == target) {
                count++;
            }
            return;
        }
        
        int plus = result + numbers[depth];
        int minus = result - numbers[depth];
        
        DFS(numbers, depth+1, target, plus);
        DFS(numbers, depth+1, target, minus);
    }
}