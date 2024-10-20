import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int n : scoville) {
            pq.offer(n);
        }
        int answer = 0;
        while(pq.peek() < K) {
            if(pq.size() >= 2) {
                int p1 = pq.poll();
                int p2 = pq.poll();  
                int res = p1 + (p2 * 2);
                pq.offer(res);
                answer ++;
            }else {
                return -1;
            }
        }
        
        return answer;
    }
}