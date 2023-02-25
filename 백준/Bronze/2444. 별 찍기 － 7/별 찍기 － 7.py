n = int(input())

for i in range(n): # 0 1 2 3 4
    for j in range(n-i-1): # 4 3 2 1 0
        print(' ', end = '')
    
    for k in range(2*i+1):
        print('*', end = '')
    print()

for i in range(1, n): # 1, 2, 3, 4
    for j in range(i):
        print(' ', end = '')
    
    for k in range((2*n)-(2*i)-1):
        print('*', end = '')
    print()