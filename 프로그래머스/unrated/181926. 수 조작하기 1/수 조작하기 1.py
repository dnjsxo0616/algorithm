def solution(n, control):
    dit = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))
    return n + sum([dit[i] for i in control])