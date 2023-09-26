def solution(array, commands):
    answer = []
    for i in commands:
        arrs = array[i[0]-1:i[1]]
        arrs.sort()
        answer.append(arrs[i[2]-1])
    return answer