def solution(a, d, included):
    numbers = [a]
    answer = 0
        
    for i in range(len(included)):
        if(included[i] == True):
            answer += d*i+a
    return answer