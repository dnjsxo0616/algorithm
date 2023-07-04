def solution(sides):
    num = max(sides)
    sides.remove(num)
    if num >= sum(sides):
        answer = 2
    else:
        answer = 1
    return answer