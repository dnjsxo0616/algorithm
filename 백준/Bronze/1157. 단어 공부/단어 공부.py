word = input()
words = word.upper()
ans = {}

for i in words:
    if i not in ans:
        ans[i] = 1
    else:
        ans[i] += 1

tmp = []
for k, v in ans.items():
    if max(ans.values())==v:
        tmp.append(k)

if len(tmp) >= 2:
    print('?')
elif len(tmp) == 1:
    print(*tmp)