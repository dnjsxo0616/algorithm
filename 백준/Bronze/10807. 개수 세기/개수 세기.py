n = int(input())
num = list(map(int, input().split()))
f = int(input())

cnt = 0
for i in num:
    if i == f:
        cnt += 1
print(cnt)