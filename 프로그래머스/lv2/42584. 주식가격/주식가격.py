from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        pre = queue.popleft()
        time = 0
        for i in queue:
            time += 1
            if i < pre:
                break
        answer.append(time)
    return answer