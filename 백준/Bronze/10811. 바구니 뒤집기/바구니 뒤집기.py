n, m = map(int, input().split())
ans = []
for i in range(1, n+1):
    ans.append(i)
for _ in range(m):
    a, b = map(int, input().split())
    ans[a-1:b] = ans[a-1:b][::-1]
print(*ans)