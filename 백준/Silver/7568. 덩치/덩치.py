n = int(input())

total = []
for _ in range(n):
    a = list(map(int, input().split()))
    total.append(a)

ans = []
for i in total:
    cnt = 1
    for j in total:
        if i[0]<j[0] and i[1]<j[1]:
            cnt +=1
    ans.append(cnt)
print(*ans)