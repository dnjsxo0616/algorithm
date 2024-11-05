import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> map = new HashMap<>();
        for(String[] cloth : clothes) {
            String c = cloth[1];
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        
        int answer = 1;
        
        for(int key : map.values()) {
            answer *= (key+1);
        }
        
        return answer-1;
    }
}