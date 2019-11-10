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
