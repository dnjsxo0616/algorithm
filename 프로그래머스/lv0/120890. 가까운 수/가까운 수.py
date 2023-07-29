def solution(array, n):
    answer = {}
    for i in array:
        if i > n:
            answer[i] = i-n
        else:
            answer[i] = n-i
    ans = [k for k,v in answer.items() if min(answer.values()) == v]
    a = sorted(ans)
    return a[0]