'''
def solution(n, s):
    if n > s:
        return [-1]
    
    a = [(s//n) for _ in range(n-(s-((s//n)*n)))]
    b = [((s//n)+1) for _ in range(s-((s//n)*n))]

    return a+b
'''

from heapq import heappop, heappush, heapify

def solution(n, s):
    if n > s:
        return [-1]
    
    heap = [int(s/n) for _ in range(n)]
    heapify(heap)
    
    for _ in range(s - sum(heap)):
        heappush(heap, heappop(heap) + 1)
        
    return sorted(heap)
