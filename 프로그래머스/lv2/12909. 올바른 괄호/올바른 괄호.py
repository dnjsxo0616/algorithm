def solution(s):
    answer = True
    
    res = []
    for i in s:
        if i == "(":
            res.append(i)
        else:
            if res:
                res.pop()
            else:
                answer = False
                break
    if res:
        answer = False
    return answer