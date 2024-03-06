def solution(n, m, section):
    answer = 0
    
    while section:
        if not section:
            return answer
        
        num = section.pop()
        answer += 1
        
        for _ in range(m):
            if not section:
                break
            if section[-1] > num-m:
                section.pop()
            else:
                break
            
    return answer
