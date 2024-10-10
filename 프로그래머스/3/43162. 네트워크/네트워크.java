import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        //n은 컴퓨터의 개수
        // 연결에대한 정보i번과 j가 연결되어 있다면 1
        for(int i=0; i<n; i++) {
            if(!visited[i]) {
                BFS(i, computers, visited);
                answer++;
            }
        }

        return answer;
    }
    public void BFS(int v, int[][] computers, boolean[] visited) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(v);
        visited[v] = true;
        
        while(!q.isEmpty()) {
            int p = q.poll();
            for(int i=0; i<computers.length; i++) {
                if(computers[p][i] == 1 && !visited[i]) {
                    q.offer(i);
                    visited[i] = true;
                }
            }
        }
        
    }
}