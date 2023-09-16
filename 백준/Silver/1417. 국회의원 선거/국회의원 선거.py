import heapq, sys
input = sys.stdin.readline

N = int(input())

h = []

for i in range(N):
    n = int(input())
    if i == 0:
        da = n
        continue
    
    heapq.heappush(h, -n)

cnt = 0

while h:
    m = -heapq.heappop(h)
    if m < da:
        break
    cnt += 1
    da += 1
    heapq.heappush(h, -(m-1))

print(cnt)