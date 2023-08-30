from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = [(p, l) for p, l in enumerate(priorities)]
    deque_p = deque(priorities)
    
    while True:
        pre = deque_p.popleft()
        if any(pre[1] < i[1] for i in deque_p):
            deque_p.append(pre)
        else:
            answer += 1
            if pre[0] == location:
                return answer