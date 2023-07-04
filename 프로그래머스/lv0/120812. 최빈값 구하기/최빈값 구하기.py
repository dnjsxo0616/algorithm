def solution(array):
    answer = {}
    for i in array:
        if i not in answer:
            answer[i] = 1
        else:
            answer[i] += 1
    res = [k for k,v in answer.items() if max(answer.values()) == v]
    if len(res) > 1:
        a = -1
    else:
        a = res[0]
    return a