def solution(nums):
    N = len(nums) // 2
    num = list(set(nums))
    return min(len(num), N)