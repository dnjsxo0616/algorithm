import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> q = new LinkedList<>();
        
        for(int i=0; i<speeds.length; i++) {
            int remainingDay = 100 - progresses[i];
            int finishDay = (int) Math.ceil((double) remainingDay / speeds[i]);
            // int finishDay = remainingDay / speeds[i];
            q.add(finishDay);
        }
        
        List<Integer> ans = new ArrayList<>();
        int count = 1;
        int firstDue = q.poll();
        
        while(!q.isEmpty()) {
            int due = q.poll();
            if(due > firstDue) {
                firstDue = due;
                ans.add(count);
                count = 1;
            } else {
                count++;
            }
        }
        
        ans.add(count);
        
        int[] answer = ans.stream().mapToInt(Integer::intValue).toArray();
        
        return answer;
        
    }
}