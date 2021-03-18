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
