N, M = map(int, input().split())

n = []
for i in range(N):
    word = input()
    n.append(word)

ans = []
for j in range(M):
    words = input()
    ans.append(words)

s_n = set(n)
s_a = set(ans)

rep = s_n & s_a
print(len(rep))
aa = sorted(rep)
for i in aa:
    print(i)