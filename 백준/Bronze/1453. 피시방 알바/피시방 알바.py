import sys
input = sys.stdin.readline

n = int(input())

seat = []
answer = []

nums = list(input().split())

for i in nums:
    if i not in seat:
        seat.append(i)
    else:
        answer.append(i)

print(len(answer))