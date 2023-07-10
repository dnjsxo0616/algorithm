import sys
import heapq
input = sys.stdin.readline

ans = []

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if ans:
            print(heapq.heappop(ans))
        else:
            print(0)
    else:
        heapq.heappush(ans, n)