import sys
input = sys.stdin.readline

n = int(input())
num = [i for i in range(1, n+1)]

while len(num)>1:
    print(num.pop(0), end = " ")
    num.append(num.pop(0))
print(num[0])