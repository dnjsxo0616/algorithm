n, m = input().split()

cnt = 0
ans = 0
for j in m:
    cnt += int(j)
for i in n:
    ans += (int(i)*cnt)
print(ans)