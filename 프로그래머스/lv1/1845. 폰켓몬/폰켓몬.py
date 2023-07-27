def solution(nums):
    res = len(set(nums))
    if len(nums) // 2 > res:
        return res
    else:
        return len(nums) // 2