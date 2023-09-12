import heapq, sys

input = sys.stdin.readline


N = int(input())
h = []

for _ in range(N):
    s = int(input())

    if s == 0:
        print(heapq.heappop(h) if h else 0)
    else:
        heapq.heappush(h, s)