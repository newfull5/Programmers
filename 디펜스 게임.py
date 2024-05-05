
from heapq import heapify, heappop, heappush
from collections import deque

def solution(n, k, enemy):
    cnt = k
    length = len(enemy)
    queue = deque(enemy)
    heap = []
    
    while queue:
        element = queue.popleft() * -1
        heappush(heap, element)
        
        if sum(heap)*-1 > n:
            if k > 0:
                k -= 1
                heappop(heap)
                
            elif k == 0:
                return len(heap) + cnt -1
            
    return length
