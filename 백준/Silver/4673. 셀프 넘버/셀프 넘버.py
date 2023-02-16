ans = []
for i in range(1, 10001):
    for j in str(i):
        i+=int(j)
    ans.append(i)

for i in range(1, 10001):
    if i not in ans:
        print(i)
    else:
        continue