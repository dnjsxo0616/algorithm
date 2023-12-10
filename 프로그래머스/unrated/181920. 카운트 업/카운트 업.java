import java.util.stream.IntStream;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int start_num, int end_num) {
        return IntStream.rangeClosed(start_num, end_num)
            .toArray();
    }
}