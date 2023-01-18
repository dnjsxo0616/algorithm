T = int(input())

for t in range(T):
    a = input().split()
    for i in a:
        a = i[::-1]
        print(a, end= " ")
    print()