import heapq, sys
input = sys.stdin.readline


N = int(input())
h = []

for _ in range(N):
    s = int(input())
    if s != 0:
        heapq.heappush(h, (abs(s), s))
    else:
        print(heapq.heappop(h)[1] if h else 0)