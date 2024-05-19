'''
#보자마자 힙으로 푸는 문제구나 하고 깨닳았다. 뭔가 조금은 성장한 느낌이다.

from heapq import heappop, heappush

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    heap = []
    for num in works:
        heappush(heap,-num)
        
    n *= -1
    while n != 0:
        heappush(heap,(heappop(heap) + 1))
        n += 1
    
    answer = 0
    for i in heap:
        answer += i**2
    
    return answer
'''
from heapq import heapify, heappush, heappop

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-work for work in works]
    heapify(works)
    
    for _ in range(n):
        heappush(works, heappop(works) + 1)
        
    return sum([work**2 for work in works])
