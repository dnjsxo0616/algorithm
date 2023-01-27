ans = []
for t in range(10):
    a = int(input())
    b=int(a%42)
    ans.append(b)
print(len(set(ans)))