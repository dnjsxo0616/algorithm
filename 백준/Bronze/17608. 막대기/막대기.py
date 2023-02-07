import sys
input = sys.stdin.readline
n = int(input())
total_bar = []

for _ in range(n):
    bar = int(input())
    total_bar.append(bar)

cnt = 0
ans = 0
for i in reversed(total_bar):
    if i > ans:
        cnt += 1
        ans = i
print(cnt)