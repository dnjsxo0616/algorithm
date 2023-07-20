import heapq

def solution(phone_book):
    answer = True
    while phone_book:
        num = heapq.heappop(phone_book)
        if num in phone_book:
            answer = False
            break
    return answer