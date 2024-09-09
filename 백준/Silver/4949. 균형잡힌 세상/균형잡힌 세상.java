import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;

        while((line = br.readLine()) != null) {
            Stack<Character> stack = new Stack<>();
            if (line.equals(".")) {
                break;
            }

            for(int i=0; i<line.length(); i++) {
                char c = line.charAt(i);
                if(c == '(' || c == '[') {
                    stack.push(c);
                    continue;
                }
                if(c == ')') {
                    if(stack.isEmpty() || stack.peek() != '(') {
                        System.out.println("no");
                        break;
                    }
                    stack.pop();
                    continue;
                }
                if(line.charAt(i) == ']') {
                    if(stack.isEmpty() || stack.peek() != '[') {
                        System.out.println("no");
                        break;
                    }
                    stack.pop();
                    continue;
                }
                if(c == '.') {
                    if(stack.isEmpty()) {
                        System.out.println("yes");
                    }else {
                        System.out.println("no");
                    }
                    break;
                }
            }
        }
    }
}