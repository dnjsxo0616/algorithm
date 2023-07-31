def solution(participant, completion):
    res = ''
    answer = {}
    for i in participant:
        if i not in answer:
            answer[i] = 1
        else:
            answer[i] += 1
    
    for i in completion:
        if i in answer:
            answer[i] -= 1
    
    for k,v in answer.items():
        if v == 1:
            res += k
    return res