n = int(input())
con = 0
for i in range(n):
    con+=1
    a, b = map(int, input().split())
    print(f"Case #{con}: {a+b}")