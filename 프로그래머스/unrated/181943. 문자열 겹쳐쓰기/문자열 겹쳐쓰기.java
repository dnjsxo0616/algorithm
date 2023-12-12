class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        int num1 = my_string.length();
        int num2 = overwrite_string.length();
        
        answer += my_string.substring(0, s) + overwrite_string + my_string.substring(num2+s,num1);
        return answer;
    }
}