import sys
input = sys.stdin.readline

dict = {}
for _ in range(int(input())):
    n, r = input().split()
    if r == 'enter':
        dict[n] = 1
    else:
        dict[n] -= 1

answer = []
for i, j in dict.items():
    if j == 1:
        answer.append(i)

answer.sort(reverse=True)
for i in answer:
    print(i)