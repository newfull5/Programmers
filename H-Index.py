def solution(citations):
    citations.sort()
    answer = [0]
    
    for i in range(0, max(citations)):
        cnt = 0
        for j in range(0, len(citations)):
            if i <= citations[j]:
                cnt += 1
        if i <= cnt:
            answer.append(i)
            
    return max(answer)
