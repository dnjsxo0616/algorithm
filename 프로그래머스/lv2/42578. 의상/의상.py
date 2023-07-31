def solution(clothes):
    res = {}
    answer = 1
    
    for i in clothes:
        if i[1] in res:
            res[i[1]] += 1
        else:
            res[i[1]] = 1

    for k, v in res.items():
        con = v + 1

        answer *= con
    return answer-1