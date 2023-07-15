def solution(n):
    i = 0
    cnt = 1
    while (n>=cnt):
        i += 1
        cnt *= i
    answer = i - 1
    return answer