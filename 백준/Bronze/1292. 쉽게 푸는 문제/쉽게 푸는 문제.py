a, b = map(int, input().split())

ans = [0]
for i in range(1, b+1):
    for j in range(i):
        ans.append(i)
print(sum(ans[a:b+1]))