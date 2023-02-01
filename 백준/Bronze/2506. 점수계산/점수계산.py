N = int(input())

score = list(map(int, input().split()))

cnt = 0
ans = 0
for i in score:
    if i == 1:
        cnt += 1
        ans += cnt
    elif i == 0:
        cnt = 0
print(ans)