A = int(input())
B = int(input())
C = int(input())
ans = [0]*10
res = str(A*B*C)


for i in res:
    for j in range(0, 10):
        if int(i) == j:
            ans[j] += 1
for i in ans:
    print(i)
            