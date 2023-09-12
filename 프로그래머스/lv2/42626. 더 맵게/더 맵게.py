import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1 and scoville[0] < K:
        res = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, res)
        answer += 1
    return answer if scoville[0] >= K else -1