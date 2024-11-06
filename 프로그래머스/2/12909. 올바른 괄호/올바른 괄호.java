import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = false;

        Stack<Character> stack = new Stack<>();
        for(int i=0; i<s.length(); i++) {
            stack.add(s.charAt(i));
        }
        
        char start = stack.pop();
        if(start == '(') {
            return answer;
        }
        
        int count = 1;
        while(!stack.isEmpty()) {
            char c = stack.pop();
            switch(c) {
                case ')':
                    count++;
                    break;
                case '(':
                    count--;
                    break;
            }

            if(count < 0) {
                return answer;
            }
        }
        
        if(count == 0) {
            answer = true;
        }
        return answer;
    }
}