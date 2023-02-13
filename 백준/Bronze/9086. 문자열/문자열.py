T = int(input())

res = []
for _ in range(T):
    n = input()
    list_n = list(n)
    ans=list_n[0]+list_n[-1]
    res.append(ans)
print(*res, sep = '\n')