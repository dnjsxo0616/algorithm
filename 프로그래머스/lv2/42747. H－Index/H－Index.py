def solution(cit):
    cit.sort(reverse=True)

    cnt = 0

    lis_cit = []
    for i in enumerate(cit):
        if i[0] < i[1]:
            cnt += 1
        else:
            break
    return cnt