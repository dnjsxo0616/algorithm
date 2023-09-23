import heapq
import sys
input = sys.stdin.readline

N = int(input())

h = []

for _ in range(N):
    s = list(map(int, input().split()))

    if s[0] == 0:
        if h:
            print(-heapq.heappop(h))
        else:
            print(-1)
    else:
        for i in range(s[0]):
            heapq.heappush(h, -s[i+1])