n = int(input())
num = input()
nums = list(map(int, str(num)))
ans = 0

for i in nums:
    # print(type(i))
    ans += i
print(ans)