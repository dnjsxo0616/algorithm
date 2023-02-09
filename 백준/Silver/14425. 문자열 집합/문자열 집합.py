n, m = map(int, input().split())

to_s = []

for _ in range(n):
    a = input()
    to_s.append(a)
cnt = 0
for _ in range(m):
    t = input()
    if t in to_s:
        cnt += 1
print(cnt)