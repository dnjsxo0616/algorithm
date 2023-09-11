import sys
input = sys.stdin.readline

import heapq

h = []

for _ in range(int(input())):
    N = int(input()) * -1
    if N == 0:
        print(heapq.heappop(h) * -1 if h else 0)
    else:
        heapq.heappush(h, N)