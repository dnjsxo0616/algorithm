def solution(n, k):
    new_k = n//10
    answer = (n*12000)+(k*2000)-(new_k * 2000)
    return answer