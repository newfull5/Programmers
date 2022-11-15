'''
def solution(people, limit):
    people.sort()
    cnt = 0
    light = 0
    heavy = len(people)-1
    
    while heavy>light: 
        if people[light] + people[heavy] > limit:
            heavy -= 1
        else:
            cnt += 1
            heavy -= 1
            light += 1
            
    return len(people) - cnt
'''
'''
#2020.04.18
def solution(people, limit):
    people.sort()
    a, b = 0, len(people)-1
    pair = 0

    while a < b:
        if people[a] + people[b] > limit:
            b -= 1
        else:
            pair += 1
            a += 1
            b -= 1
    return len(people)-pair
'''
#2022.11.14
from heapq import heapify, heappop

def solution(people, limit):
    length = len(people)
    
    if length == 1:
        return 1
    
    max_heap = [-v for v in people]
    heapify(max_heap)
    heapify(people)
    answer = 0
    
    while length > 0:
        small_people = heappop(people)
        length -= 1
        for _ in range(length):
            if length == 0:
                break
            big_people = -heappop(max_heap)
            length -= 1
            answer += 1
            if big_people + small_people <= limit:
                break
        else:
            answer += 1
            
    return answer
