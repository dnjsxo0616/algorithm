n = int(input())
res = 0
for i in range(n):
    a = sum(list(map(int, str(i))))
    if n == a+i:
        res = i
        break
print(res)