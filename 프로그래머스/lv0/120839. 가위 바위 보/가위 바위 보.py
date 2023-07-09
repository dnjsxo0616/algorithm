def solution(rsp):
    arr = {'2':'0', '0':'5', '5':'2'}
    return ''.join(arr[i] for i in rsp)