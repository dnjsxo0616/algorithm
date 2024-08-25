import java.util.*;

public class Main {
    static List<Integer>[] graph;
    static boolean[] visited;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 정점 개수
        int m = sc.nextInt(); // 간선의 개수

        graph = new ArrayList[n + 1];
        visited = new boolean[n+1];

        for(int i=0; i<=n; i++) {
            graph[i] = new ArrayList<>();
        }

        for(int i=0; i<m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            graph[a].add(b);
            graph[b].add(a);
        }

        int count = 0;
        for(int i=1; i<=n; i++) {
            if(!visited[i]) {
                DFS(i);
                count++;
            }
        }

        System.out.print(count);

    }

    public static void DFS(int node) {
        visited[node] = true;

        for(int s : graph[node]) {
            if(!visited[s]) {
                DFS(s);
            }
        }
    }
}