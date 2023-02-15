N = int(input())
num = list(map(int, input().split()))

num.sort()
cnt = 0
res = 0
ans = []
for i in num:
    cnt = res + i
    res = cnt
    ans.append(cnt)
print(sum(ans))