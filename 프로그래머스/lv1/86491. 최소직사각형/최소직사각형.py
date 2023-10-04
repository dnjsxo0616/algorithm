def solution(sizes):
    h_size = []
    l_size = []

    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            h_size.append(sizes[i][0])
            l_size.append(sizes[i][1])
        else:
            h_size.append(sizes[i][1])
            l_size.append(sizes[i][0])
    return max(h_size) * max(l_size)