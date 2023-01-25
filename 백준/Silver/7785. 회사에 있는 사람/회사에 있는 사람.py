n = int(input())

ans = {}

for i in range(n):
    a, b = input().split()
    if b == "enter" :
        ans[a] = b
    else:
        del ans[a]
        
ans = sorted(ans.keys(), reverse = True)
for i in ans:
    print(i)