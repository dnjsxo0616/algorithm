import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class Main {
	static char[][] board;


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		board = new char[n][m];
		
		for(int i=0; i<n; i++) {
			board[i] = br.readLine().toCharArray();
		}
		
		int minCount = 64;
		
		for (int i = 0; i <= n - 8; i++) {
            for (int j = 0; j <= m - 8; j++) {
                minCount = Math.min(minCount, find(i, j));
            }
        }
		System.out.println(minCount);

	}
	
	public static int find(int x, int y) {
		String[] pattern1 = {"WBWBWBWB", "BWBWBWBW"};
		String[] pattern2 = {"BWBWBWBW", "WBWBWBWB"};
		
		int count1 = 0;
		int count2 = 0;
		
		for(int i=0; i<8; i++) {
			for(int j=0; j<8; j++) {
				if(board[x + i][y+j] != pattern1[i%2].charAt(j)){
					count1++;
				}
				if (board[x + i][y + j] != pattern2[i % 2].charAt(j)) {
                    count2++;
                }
			}
		}
		return Math.min(count1, count2);
	}

}
