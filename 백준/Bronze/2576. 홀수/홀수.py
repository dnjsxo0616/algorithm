cnt = 0
nums = []

for i in range(7):
    num = int(input())
    if num%2 == 1:
        cnt += num
        nums.append(num)

if not nums:
    print(-1)
else:
    m = nums[0]
    for j in nums:
        if j<m:
            m = j
    print(cnt)
    print(m)