def solution(balls, share):
    ball = 1
    for i in range(balls, balls-share, -1):
        ball *= i
    sh = 1
    for i in range(1, share+1):
        sh *= i
    answer = ball//sh
    return answer