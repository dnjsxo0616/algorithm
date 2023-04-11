n = int(input())

dit = {}
for i in range(n):
    word = input()
    if word not in dit:
        dit[word] = 1
    else:
        dit[word] += 1
# print(dit)
arr = dict(sorted(dit.items()))
# print(arr)
for k,v in arr.items():
    if max(arr.values()) == v:
        print(k)
        break