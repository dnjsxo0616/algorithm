def solution(nums):
    answer = len(nums) // 2
    nums = set(nums)
    res = min(answer, len(nums))
    return res