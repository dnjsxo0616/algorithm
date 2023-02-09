n, m = map(int, input().split())

numbers = list(map(int, input().split()))
ans = []
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
           sun = numbers[i] + numbers[j] + numbers[k]
           if sun <= m:
               ans.append(sun)
print(max(ans))