T = int(input())


for t in range(T):
    cnt = 0
    ans = 0
    n = input()
    for i in n:
        if i =='O':
            cnt += 1
            ans += cnt
        elif i == 'X':
            cnt = 0
    print(ans)