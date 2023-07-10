import sys
import heapq
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    N = int(input())
    if N == 0:
        if ans:
            print(heapq.heappop(ans)[1])
        else:
            print(0)
    else:
        heapq.heappush(ans, (abs(N), N))