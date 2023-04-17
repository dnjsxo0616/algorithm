nums = 0
for _ in range(10):
    num = int(input())
    pre_num = nums
    nums += num
    if nums >= 100:
        if nums - 100 > 100 - pre_num:
            nums = pre_num
        break
print(nums)