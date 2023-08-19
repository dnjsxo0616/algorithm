import sys
input = sys.stdin.readline

x = int(input())

for i in range(x, 0, -1):
    print('*'*i)