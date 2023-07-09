def solution(rsp):
    arr = {'2':'0', '0':'5', '5':'2'}
    answer = rsp.translate(str.maketrans(arr))
    return answer