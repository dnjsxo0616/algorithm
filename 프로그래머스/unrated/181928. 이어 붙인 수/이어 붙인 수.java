class Solution {
    public int solution(int[] num_list) {
        String even = "";
        String odd = "";
        for(int number : num_list) {
            if(number%2 == 0) {
                even += String.valueOf(number);
            } else if(number%2 == 1) {
                odd += String.valueOf(number);
            }
        }
        
        int answer = Integer.parseInt(even) +  Integer.parseInt(odd);
       
        return answer;
    }
}