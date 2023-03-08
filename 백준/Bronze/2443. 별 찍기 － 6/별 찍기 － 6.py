n = int(input())

for i in range(n): # 0 1 2 3 4
    for j in range(i): # 0 1 2 3 4
        print(' ', end = '')
    for k in range((2*n)-(2*i)-1):
        print('*', end = '')
    print()