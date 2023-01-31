a = []
for _ in range(28):
    n = int(input())
    a.append(n)
ans = list(range(1, 31))

for i in a:
    ans.remove(i)
print(*ans, sep = '\n')