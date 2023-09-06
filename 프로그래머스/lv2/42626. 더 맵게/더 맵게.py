import heapq

def solution(scoville, K):
    scoville.sort()
    answer = 0
    heapq.heapify(scoville)
    
    if scoville[0] >= K:
        return answer
    while len(scoville) > 1 and scoville[0] < K:
        answer += 1
        pre = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, pre)
    
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    return answer