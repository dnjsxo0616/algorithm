def solution(hp):
    one = hp // 5
    hp = hp - (one * 5)
    two = hp // 3
    hp = hp - (two * 3)
    answer = one + two + hp
    return answer