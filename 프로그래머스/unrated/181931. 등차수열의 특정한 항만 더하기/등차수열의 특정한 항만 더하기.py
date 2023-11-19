def solution(a, d, included):
    numbers = [a]
    answer = 0

    for i in range(len(included)-1):
        numbers.append(numbers[i]+d)
        
    for i in range(len(included)):
        if(included[i] == True):
            answer += numbers[i]
    return answer