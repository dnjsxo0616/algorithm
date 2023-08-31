from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0 for i in range(bridge_length)])
    truck_weights = deque(truck_weights)
    
    cnt = 0
    while truck_weights:
        time += 1
        cnt -= bridge.popleft()
        
        if cnt + truck_weights[0] <= weight:
            cnt += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
    
    time += bridge_length
        
    return time