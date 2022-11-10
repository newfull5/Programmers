def solution(k, m, score):
    answer = 0
    score.sort()
    
    while len(score) >= m:
        answer += min([score.pop() for _ in range(m)])*m
        
    return answer
