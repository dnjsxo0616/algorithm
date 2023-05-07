arr = []
lens = []
for _ in range(5):
    word = input()
    arr.append(word)
    lens.append(len(word))


ans = ''
for i in range(max(lens)):
    for j in range(5):
        if i < lens[j]:
            ans += arr[j][i]
print(ans)