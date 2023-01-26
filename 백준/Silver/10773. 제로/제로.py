T = int(input())

ans = []
for t in range(T):
    n = int(input())
    if n == 0:
        ans.pop()
    else:
        ans.append(n)
print(sum(ans))