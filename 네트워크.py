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
