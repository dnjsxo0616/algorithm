n, m = map(int, input().split())

s = []

for _ in range(n):
    a = input()
    s.append(a)
S = set(s)
cnt = 0
for _ in range(m):
    t = input()
    if t in S:
        cnt += 1
print(cnt)