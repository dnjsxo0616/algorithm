
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

h= deque([])

for _ in range(N):
    s = input().split()

    if s[0] == 'push':
        h.append(s[1])
    elif s[0] == 'pop':
        if h:
            print(h.popleft())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(h))
    elif s[0] == 'empty':
        if h:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if h:
            print(h[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if h:
            print(h[-1])
        else:
            print(-1)