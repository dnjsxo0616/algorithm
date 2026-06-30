import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        Map<Character, Integer> map = new HashMap<>();
        
        for (String key : keymap) {
            for (int i=0; i<key.length(); i++) {
                char c = key.charAt(i);
                int cont = i + 1;
                
                if (!map.containsKey(c)) {
                    map.put(c, cont);
                } else {
                    map.put(c, Math.min(map.get(c), cont));
                }
            }
        }
        int[] answer = new int[targets.length];
        
        for(int i=0; i<targets.length; i++) {
            String target = targets[i];
            int sum = 0;
            boolean imp = false;
            
            for (int j=0; j<target.length(); j++) {
                char c = target.charAt(j);
                
                if(!map.containsKey(c)) {
                    imp = true;
                    break;
                }
                
                sum += map.get(c);
            }
            
            if(imp) {
                answer[i] = -1;
            } else {
                answer[i] = sum;
            }
        }
        return answer;
    }
}