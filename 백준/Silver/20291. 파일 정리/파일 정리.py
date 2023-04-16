n = int(input())

arr = {}
for _ in range(n):
    word = input().split('.')
    if word[1] not in arr:
        arr[word[1]] = 1
    elif word[1] in arr:
        arr[word[1]] += 1
dic_arr = dict(sorted(arr.items()))

for k, v in dic_arr.items():
    print(k, v)