T= int(input())
ans = []

for t in range(1, T+1):
    n = int(input())
    if n != 0:
        ans.append(n)
    elif n == 0:
        ans.pop()
print(sum(ans))