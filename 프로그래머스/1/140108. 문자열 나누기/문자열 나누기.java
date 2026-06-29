class Solution {
    public int solution(String s) {
        int answer = 0;
        
        char x = s.charAt(0);
        int same = 0;
        int dif = 0;
        
        for(int i=0; i<s.length(); i++) {
            if(same == 0 && dif == 0) {
                x = s.charAt(i);
            }
            
            if(s.charAt(i) == x) {
                same++;
            } else {
                dif++;
            }
            
            if(same == dif) {
                answer++;
                same = 0;
                dif = 0;
            }
        }
        
        if(same != 0 || dif != 0) {
            answer++;
        }
        return answer;
    }
}