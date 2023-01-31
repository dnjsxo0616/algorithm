n = int(input())

star = '*'
res=[]
for i in range(n):
    a=(' '*i) + (star*n)
    res.append(a)
    n -= 1
print(*res, sep = '\n')