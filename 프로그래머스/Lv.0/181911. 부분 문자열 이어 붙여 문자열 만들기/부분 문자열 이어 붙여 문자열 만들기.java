class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        String answer = "";
        for(int i=0; i<my_strings.length; i++) {
            int[] pos = parts[i];
            answer += my_strings[i].substring(pos[0], pos[1]+1);
        }
        return answer;
    }
}