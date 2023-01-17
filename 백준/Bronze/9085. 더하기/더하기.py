T = int(input())
ans = 0
result = []
for t in range(1, T+1):
    a = int(input())
    num = list(map(int, input().split()))
    for i in num:
        ans += i
    result.append(ans)
    ans = 0
print(*result, sep = '\n')