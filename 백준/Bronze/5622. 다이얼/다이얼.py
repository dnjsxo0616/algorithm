n = input()
list_n = list(n)
ans = {
    3:['A', 'B', 'C'],
    4:['D', 'E', 'F'],
    5:['G', 'H', 'I'],
    6:['J', 'K', 'L'],
    7:['M', 'N', 'O'],
    8:['P', 'Q', 'R', 'S'],
    9:['T', 'U', 'V'],
    10:['W', 'X', 'Y', 'Z']
}
cnt = 0
for word in list_n:
    for k, v in ans.items():
        if word in v:
            cnt += k
print(cnt)