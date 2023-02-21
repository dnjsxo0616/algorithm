N, M = map(int, input().split())

ans = [0 for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    for i in range(a-1, b):
        ans[i] = c
print(*ans)
