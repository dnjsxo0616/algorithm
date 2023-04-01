def solution(money):
    answer = []
    change = 0
    n = 0
    ice = 5500
    change = money//ice
    n = money - (ice*change)
    answer.append(change)
    answer.append(n)
    return answer