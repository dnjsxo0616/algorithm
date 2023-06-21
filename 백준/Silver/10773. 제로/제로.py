import sys
input = sys.stdin.readline

n = int(input())

ans = []
for _ in range(n):
    num = int(input())
    if num != 0:
        ans.append(num)
    else:
        ans.pop()

print(sum(ans))