import numpy as np

def get_directions(current_node, height, width, maps, visited):
    answer = []
    row,col = current_node
    if row != 0: # Up
        if maps[row-1, col] != 'X' and [row-1, col] not in visited:
            answer.append([row-1, col])
    if row != height-1: # Down
        if maps[row+1, col] != 'X' and [row+1, col] not in visited:
            answer.append([row+1, col])
    if col != 0: # LEFT
        if maps[row, col-1] != 'X' and [row, col-1] not in visited:
            answer.append([row, col-1])
    if col != width-1: # RIGHT
        if maps[row, col+1] != 'X' and [row, col+1] not in visited:
            answer.append([row, col+1])
    return answer



def solution(maps):
    
    answer = 0
    height = len(maps)
    width = len(maps[0])
    maps = np.array([list(m) for m in maps])
    
    r,c = np.where(maps == 'S')
    start_node = [int(r),int(c)]
    
    r,c = np.where(maps == 'E')
    exit_node = [int(r),int(c)]
    
    r,c = np.where(maps == 'L')
    lever_node = [int(r),int(c)]
    
    stack = [start_node]
    visited = []
    
    def dfs(current_node, visited, maps, cnt, types):
        nonlocal answer
        visited.append(current_node)
        if types == 'lever':
            if current_node == lever_node:
                answer += cnt
                return
        elif types == 'exit':
            if current_node == exit_node:
                answer += cnt
                return
        for node in get_directions(current_node, height, width, maps, visited):
            dfs(node, visited, maps, cnt+1, types)
            
    dfs(start_node, visited, maps, 0, 'lever')
    if answer == 0:
        return -1
    temp_answer = answer
    dfs(lever_node, visited, maps, 0, 'exit')
    if temp_answer == answer:
        return -1
    
    return answer
