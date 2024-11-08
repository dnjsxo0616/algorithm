import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> q = new LinkedList<>();
        for(int i=0; i<bridge_length-1; i++) {
            q.offer(0);
        }
        
        int currentW = truck_weights[0];
        q.add(currentW);
        
        int index = 1;
        int answer = 1;
        while(!q.isEmpty()) {
            answer++;
            
            int bridgeTruck = q.poll();
            currentW -= bridgeTruck;
            
            if(index < truck_weights.length) {
                if(currentW + truck_weights[index] <= weight) {
                    currentW += truck_weights[index];
                    q.add(truck_weights[index]);
                    index++;
                }else {
                    q.offer(0);
                }
            }
        }
        
        return answer;
    }
}