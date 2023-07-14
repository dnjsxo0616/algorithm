def solution(participant, completion):
    answer = []
    part = {}
    for i in participant:
        if i in part:
            part[i] += 1
        else:
            part[i] = 1
    com = {}
    for i in completion:
        if i in com:
            com[i] += 1
        else:
            com[i] = 1
    for key in part:
        if key not in com or part[key] != com[key]:
            answer = key
    return answer