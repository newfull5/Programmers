"""
# 2020.7.20
def solution(n, computers):
    answer = 0
    visit = []
    
    def dfs(current):
        nonlocal visit
        nonlocal n
        nonlocal computers

        visit.append(current)

        for i in range(n):
            if computers[current][i] == 1 and (i not in visit):
                dfs(i)

        return visit

    for i in range(n):
        if i not in visit:
            answer += 1
            dfs(i)
            
    return answer
"""
"""
# 2021.3.18
def solution(n, computers):
    visited = []

    answer = 0

    def DFS(i):
        nonlocal visited
        visited.append(i)

        for index in range(n):
            if computers[i][index] == 1 and index not in visited:
                DFS(index)
        else:
            return

    for i in range(n):
        for j in range(n):
            if j not in visited and computers[i][j] == 1:
                DFS(i)
                answer += 1

    return answer
"""
'''
#2021.6.24
def solution(n, computers):
    
    visited = []

    answer = 0

    def DFS(idx):

        nonlocal visited

        visited.append(idx)

        for i,v in enumerate(computers[idx]):
            if v == 1 and i not in visited:
                DFS(i)

    for index in range(n):
        if index not in visited:
            answer += 1
            DFS(index)

    return answer
'''
def solution(n, computers):
    visited = []
    answer = []
    
    def dfs(start_node, visited, answer):
        visited.append(start_node)
        answer.append(start_node)
        for i, v in enumerate(computers[start_node]):
            if i in visited or v == 0:
                continue
            visited, answer = dfs(i, visited, answer)
            
        return visited, answer
        
    for i in range(len(computers)):
        if i in visited:
            continue
        visited, network = dfs(i, visited, [])
        answer.append(network)
        
    return len(answer)
