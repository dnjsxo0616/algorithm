N, X = map(int, input().split())
num = list(map(int, input().split()))

result = []

for i in num:
    if i<X:
        result.append(i)
for j in result:
    print(j, end = " ")