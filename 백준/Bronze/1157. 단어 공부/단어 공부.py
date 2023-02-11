n = input()
up_n = n.upper()

list_n = list(up_n)


ans = {}
for i in list_n:
    if i not in ans:
        ans[i] = 1
    else:
        ans[i] += 1

# tmp = [key for key, value in ans.items() if max(ans.values()) == value]
tmp = []
for key, value in ans.items():
    if max(ans.values()) == value:
        tmp.append(key)
if len(tmp) > 1:
    print('?')
else:
    print(*tmp)