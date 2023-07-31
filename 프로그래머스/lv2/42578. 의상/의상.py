def solution(clothes):
    res = {}
    answer = 1
    
    for clothe, types in clothes:
        res[types] = res.get(types, 0) +1
    
    for i in res:
        answer *= (res[i] + 1)
        
    return answer-1