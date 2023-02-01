n, m = list(map(int, input().split()))
num = list(map(int, input().split()))

#3장씩 m이 넘지않는 최대수
ans = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            total = num[i] + num[j] + num[k]
            if total <= m:
                ans.append(total)
print(max(ans))