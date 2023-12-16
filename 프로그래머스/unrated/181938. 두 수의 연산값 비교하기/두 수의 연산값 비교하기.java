class Solution {
    public int solution(int a, int b) {
        
        int plus = Integer.parseInt(""+a+b);
        int multiple = 2 * a * b;
        return plus > multiple ? plus : multiple;
    }
}