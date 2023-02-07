lis ={}
n = int(input())

for _ in range(n):
    a, b = input().split()
    if b == 'enter':
        lis[a] = b
    else:
        del lis[a]

ans = sorted(lis, reverse=True)
for i in ans:
    print(i)
