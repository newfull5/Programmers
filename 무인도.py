import numpy as np
from collections import deque

def get_linked_element(i,j, maps, visited):
    max_height = len(maps)-1
    max_width = len(maps[0])-1
    
    queue = deque([[i,j]])
    linked_element = []
    
    while queue:
        i,j = queue.popleft()
        if [i,j] in visited:
            continue
        visited.append([i,j])
        linked_element.append([i,j])
        
        # UP
        if i != 0:
            if maps[i-1, j] != 'X' and [i-1, j] not in visited:
                queue.append([i-1, j])
        # LEFT
        if j != 0:
            if maps[i, j-1] != 'X' and [i, j-1] not in visited:
                queue.append([i, j-1])
        # RIGHT
        if [i, j+1] not in visited and j != max_width:
            if maps[i, j+1] != 'X':
                queue.append([i, j+1])
        # DOWN
        if [i+1, j] not in visited and i != max_height:
            if maps[i+1, j] != 'X':
                queue.append([i+1, j])
            
        
    return sum([int(maps[i,j]) for i,j in linked_element]), visited


def solution(maps):
    visited = []
    answer = []
    maps = np.array([list(t) for t in maps])
    
    (get_linked_element(3,0, maps, visited))
    for i in range(len(maps)):
        for j in range(len(maps)):
            if maps[i,j] == 'X':
                visited.append([i,j])
                
