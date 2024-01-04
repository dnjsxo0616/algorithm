class Solution {
    public int solution(int n) {
        int answer = 1;
        while(true) {
            int x = n%answer;
            if(x==1) {
               return answer;
            }
            answer++;
        }
    }
}