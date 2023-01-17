ans = []
for i in range(9):
    a = int(input())
    ans.append(a)

print(max(ans), ans.index(max(ans))+1 , sep = "\n")