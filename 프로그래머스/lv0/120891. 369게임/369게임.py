def solution(order):
    arr = [3, 6, 9]
    answer = 0
    
    str_order = str(order)
    lens_order = len(str(order))
    for i in range(lens_order):
        if int(str_order[i]) in arr:
            answer += 1
    return answer