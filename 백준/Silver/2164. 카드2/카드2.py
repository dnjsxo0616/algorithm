
from collections import deque

N = int(input())
Card = deque([i for i in range(1, N+1)])

# 1 2 3 4 5 6
while len(Card) > 1:
    Card.popleft()
    Card.append(Card.popleft())

print(Card[0])