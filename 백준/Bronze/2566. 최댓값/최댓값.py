matrix = []
for _ in range(9):
    line = list(map(int, input().split()))
    matrix.append(line)

ans = 0
a = 0
b = 0
for i in range(9):
    for j in range(9):
        if matrix[i][j] > ans:
            ans = matrix[i][j]
            a = i
            b = j
print(ans)
print(a+1, b+1)