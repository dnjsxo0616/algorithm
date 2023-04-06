N, K = map(int, input().split())
ans = K
rep = 0
money = []
for _ in range(N):
    m = int(input())
    money.append(m)
money.sort(reverse=True)


for i in money:    
    cnt = ans//i # 동전개수
    ans -= (i*cnt) # 잔돈
    rep += cnt
    if ans == 0:
        break
print(rep)