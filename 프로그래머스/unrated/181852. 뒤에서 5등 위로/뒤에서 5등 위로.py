def solution(num_list):
    answer = []
    num_list.sort(reverse=True)
    for i in range(len(num_list)-5):
        answer.append(num_list[i])
    answer.sort()
    return answer