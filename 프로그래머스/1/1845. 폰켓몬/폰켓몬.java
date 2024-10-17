import java.util.*;

class Solution {
    public int solution(int[] nums) {
        //n -> n/2 가져가
        // 그러면 4마리가 있으면 2마리를 가져가야해
        // 중복제거 후 만약 setSize가 더 작다면 이게 답
        int take = nums.length/2;
        
        Set<Integer> set = new HashSet<>();
        for(int n : nums) {
            set.add(n);
        }
        int setSize = set.size();
        
        int answer = take > setSize ? setSize : take;
        
        return answer;
    }
}