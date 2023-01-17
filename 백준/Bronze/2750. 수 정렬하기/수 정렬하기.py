T = int(input())
ans = []

for t in range(T):
    num = int(input())
    ans.append(num)
ans.sort()
for i in ans:
    print(i)