import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int res = 0;
        Stack<Integer> stack = new Stack<>();
        for(int m : moves) {
            // 내가 찾아야 하는 세로 값
            int col = m-1;

            for(int row=0; row<board[col].length; row++) {
                if(board[row][col] != 0) {
                    int a = board[row][col];
                    board[row][col] = 0;
                    if(stack.isEmpty()) {
                        stack.push(a);
                        break;
                    }
                    if(stack.peek() == a) {
                        stack.pop();
                        res += 1;
                        break;
                    }
                    stack.push(a);
                    break;
                }
            }
        }

        return res*2;
    }
}