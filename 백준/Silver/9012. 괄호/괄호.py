T = int(input())

for t in range(T):
    tx = input()
    cnt = 0

    for i in tx:
        if i == '(':
            cnt += 1
            if cnt < 0:
                print('NO')
                break
        elif i == ')':
            cnt -= 1
            if cnt < 0:
                print('NO')
                break
    if cnt == 0:
        print('YES')
    elif cnt >0:
        print('NO')