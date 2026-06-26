class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for(int i=left; i<=right; i++) {
            int n = meth(i);
            if(n%2 == 0) {
                answer += i;
            } else {
                answer-= i;
            }
        }
        return answer;
    }
    
    public int meth(int num) {
        int ans = 0;
        for(int i=1; i<=num; i++) {
            if(num % i == 0) {
                ans += 1;
            }
        }
        return ans;
    }
}