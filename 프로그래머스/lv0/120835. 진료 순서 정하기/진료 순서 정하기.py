def solution(emergency):
    answer = []
    arr= {}
    res = sorted(emergency, reverse=True)
    ind = 1
    for i in res:
        arr[i] = ind
        ind += 1
    for j in emergency:
        answer.append(arr[j])
    return answer