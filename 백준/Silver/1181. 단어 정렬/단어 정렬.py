T = int(input())

ans = []
for t in range(T):
    n = input()
    ans.append(n)
res = set(ans)
res1 = list(res)
res1.sort()
res1.sort(key=len)
for i in res1:
    print(i)