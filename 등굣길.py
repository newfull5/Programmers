def solution(m, n, puddles):
    roads = [[0]*(m+1) for _ in range(n+1)]
    roads[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            elif [j,i] in puddles:
                continue
            else:
                roads[i][j] = roads[i-1][j] + roads[i][j-1]

    return roads[n][m] % 1000000007
