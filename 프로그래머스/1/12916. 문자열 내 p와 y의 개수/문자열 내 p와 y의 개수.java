class Solution {
    boolean solution(String s) {
        s = s.toLowerCase();
 
        boolean answer = true;

        int pnum = 0;
        int ynum = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'p') {
                pnum++;
            } else if (c == 'y') {
                ynum++;
            }
        }
        
        if(pnum != ynum) {
            answer = false;
        }

        return answer;
    }
}