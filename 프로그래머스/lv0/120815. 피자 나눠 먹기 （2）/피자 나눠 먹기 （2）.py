def solution(n):
    p = 6
    while p%n !=0:
        p += 6
    answer = p//6 
    return answer