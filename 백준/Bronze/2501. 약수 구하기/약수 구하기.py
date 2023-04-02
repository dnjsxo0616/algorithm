n, m = map(int, input().split())
ans = []
for i in range(1, n+1):
    if n%i==0:
        ans.append(i)

if len(ans) >= m:
    print(ans[m-1])
else:
    print(0)