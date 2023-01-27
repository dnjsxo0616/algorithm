cnt = 0
while True:
    n = input()
    if n == '문제':
        cnt += 1
    elif n == '고무오리':
        if cnt > 0:
            cnt -= 1
        else:
            cnt += 2
    elif n == '고무오리 디버깅 끝':
        if cnt == 0:
            print('고무오리야 사랑해')
            break
        else:
            print('힝구')
            break