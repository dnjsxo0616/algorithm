class Solution {
    public int solution(int a, int b) {
        String sum1 = String.valueOf(a) + String.valueOf(b);
        String sum2 = String.valueOf(b) + String.valueOf(a);
        if(Integer.parseInt(sum1) > Integer.parseInt(sum2)){
            return Integer.parseInt(sum1);
        } else {
            return Integer.parseInt(sum2);
        }
    }
}