'''
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
'''
"""
#2020.02.26
import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        cnt += 1
        heapq.heappush(scoville, (heapq.heappop(scoville)+heapq.heappop(scoville)*2))
        
    return cnt

"""
"""
#2020.12.02
import heapq

def solution(scoville, K):
    cnt = 0
    
    heapq.heapify(scoville)
    
    while True:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        heapq.heappush(scoville, (first + second*2))

        cnt += 1
        
        if scoville[0] >= K:
            return cnt
        
        if len(scoville) == 1:
            return -1
        
"""
'''
#2021.02.27
from heapq import heappop, heapify, heappush

def solution(scoville, K):
    heapify(scoville)

    for i in range(1000000):
        if scoville[0] >= K:
            return i
        if len(scoville) < 2:
            return -1
        heappush(scoville, (heappop(scoville) + heappop(scoville) * 2))
'''     
'''
#2021.06.23
from heapq import heappop, heappush, heapify

def solution(scoville, K):

    heapify(scoville)

    cnt = 0

    while True:
        if scoville[0] >= K:
            return cnt
        
        if len(scoville) == 1:
            return -1
        
        heappush(scoville, (heappop(scoville) + heappop(scoville)*2))
        cnt += 1
'''
'''
#2022.11.19
from heapq import heapify, heappop, heappush

def solution(scoville, k):
    heapify(scoville)
    answer = 0
    
    while len(scoville) > 1:
        food1 = heappop(scoville)
        food2 = heappop(scoville)
        heappush(scoville, food1 + food2*2)
        answer += 1
        if scoville[0] >= k:
            return answer
        
    return -1
'''
from heapq import heapify, heappop, heappush

def solution(scoville, k):
    answer = 0
    heapify(scoville)
    
    while scoville[0] < k:
        if len(scoville) < 2:
            return -1
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville, a+b*2)
        answer += 1
        
    return answer
