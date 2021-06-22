"""
from collections import deque

def solution(priorities, location):
    
    trashcan = []
    abc = deque(zip(priorities,range(len(priorities))))
    
    while True:
        while abc[0][0] != max(priorities):
            abc.append(abc.popleft())

        trashcan.append(abc.popleft())
        priorities.remove(max(priorities))

        if not abc:
            break

    for i in range(0,len(trashcan)):
        if trashcan[i][1] == location:
            return i+1
"""
#2022.6.22
def solution(priorities, location):
    priorities = [(v,i) for i,v in enumerate(priorities)]

    max_p = max([a for a,b in priorities])

    cnt = 0

    while priorities:
        num, idx = priorities.pop(0)

        if num == max_p:
            cnt += 1
            
            if idx == location:
                return cnt
            
            max_p = max([a for a,b in priorities])
            
        else:
            priorities.append([num,idx])
