from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque(priorities)
    
    lot = [0 for i in range(len(priorities))]
    lot[location] = 1
    
    lot = deque(lot)
    
    cnt = 0
    while lot:
        priority = que.popleft()
        check_lot = lot.popleft()
        
        if len(que) > 1 and max(que) > priority:
            que.append(priority)
            lot.append(check_lot)
            
        else:
            cnt += 1
            if check_lot == 1:
                answer = cnt
                break
        
    return answer
