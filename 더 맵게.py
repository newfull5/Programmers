import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K:
        a, b = min(scoville[0],scoville[1]),max(heapq.heappop(scoville),heapq.heappop(scoville))
        heapq.heappush(scoville, (a+b*2) )
        cnt += 1
        if len(scoville) == 1:
            if scoville[0] < K:
                return -1
        elif scoville[0] > K:
            return cnt
