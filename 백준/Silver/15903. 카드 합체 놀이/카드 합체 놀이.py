import heapq, sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

h = list(map(int, input().split()))

Card = []

for i in h:
    heapq.heappush(Card, i)

cnt = 0

while cnt < m:
    first = heapq.heappop(Card)
    two = heapq.heappop(Card)

    res = first + two

    heapq.heappush(Card, res)
    heapq.heappush(Card, res)

    cnt += 1

print(sum(Card))