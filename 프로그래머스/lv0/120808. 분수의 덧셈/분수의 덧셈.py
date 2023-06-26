def solution(numer1, denom1, numer2, denom2):
    numer = numer1*denom2 + numer2*denom1
    denom = denom1*denom2
    for i in range(denom, 1, -1):
        if denom%i == 0 and numer%i ==0:
            denom = denom//i
            numer = numer//i
    answer = [numer, denom]
    return answer