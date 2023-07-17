def solution(my_string):
    res = ('a', 'e', 'i', 'o', 'u')
    for i in res:
        my_string = my_string.replace(i, '')
    return my_string