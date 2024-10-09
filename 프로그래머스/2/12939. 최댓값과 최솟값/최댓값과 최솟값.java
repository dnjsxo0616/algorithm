import java.util.*;

class Solution {
    public String solution(String s) {
        List<Integer> list = new ArrayList<>();
        String[] str = s.split(" ");
        for(String ss : str) {
            list.add(Integer.parseInt(ss));
        }
        int maxNumber = Collections.max(list);
        int minNumber = Collections.min(list);
        String answer = "";
        answer += String.valueOf(minNumber);
        answer += " ";
        answer += String.valueOf(maxNumber);
        return answer;
    }
}