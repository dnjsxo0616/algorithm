class Solution {
    public int solution(int n) {
        int answer = 0;
        if(n%2==1){
            for(int i=1; i<=n; i++){
                if(i%2==1){
                    answer+=i;
                }
            }
        }
        
        if(n%2==0){
            for(int i=1; i<=n; i++){
                if(i%2==0){
                    double pownum = Math.pow(i,2);
                    answer += (int) pownum;
                }
            }
        }
        return answer;
    }
}