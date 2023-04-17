n = int(input())
arr = list(map(int, input().split()))

rep = []
ans = 0
for i in range(n-1): # 0 1 2 3 4
    if arr[i] < arr[i+1]:
        ans += arr[i+1] - arr[i]
    else:
        rep.append(ans)
        ans = 0
rep.append(ans)
print(max(rep))