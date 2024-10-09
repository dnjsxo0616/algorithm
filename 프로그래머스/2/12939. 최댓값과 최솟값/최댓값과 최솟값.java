import java.util.*;

class Solution {
    public String solution(String s) {
        String[] str = s.split(" ");
        int maxNumber = Integer.MIN_VALUE;
        int minNumber = Integer.MAX_VALUE;
        
        for(String ss : str) {
            int n = Integer.parseInt(ss);
            if(n > maxNumber) {
                maxNumber = n;
            }
            if(n < minNumber) {
                minNumber = n;
            }
        }
        
        StringBuilder answer = new StringBuilder();
        answer.append(minNumber).append(" ").append(maxNumber);
        return answer.toString();
    }
}