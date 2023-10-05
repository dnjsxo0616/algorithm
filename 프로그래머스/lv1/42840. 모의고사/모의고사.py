def solution(answers):
    f, t, h = 0, 0, 0
    first = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        c1 = i % 5
        c2 = i % 8
        c3 = i % 10

        if first[c1] == answers[i]:
            f += 1
        if two[c2] == answers[i]:
            t += 1
        if three[c3] == answers[i]:
            h += 1
    
    m = max(f, t, h)
    res = []

    if m == f:
        res.append(1)
    if m == t:
        res.append(2)
    if m == h:
        res.append(3)
        
    return res
