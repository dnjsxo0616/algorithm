def solution(s):
    s = list(s.split(' '))
    answer = []
    for i in s:
        if i == 'Z':
            answer.pop()
        else:
            answer.append(int(i))
    return sum(answer)