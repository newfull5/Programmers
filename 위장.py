def solution(clothes):
    kind = []
    answer = []
    temp = ''
    
    for arr in clothes:
        if temp != arr[-1]:
            temp = arr[-1]
            kind.append(temp)
            
    kind = list(set(kind))
    
    for i in range(0,len(kind)):
        cnt = 0
        for arr in clothes:
            if arr[-1] == kind[i]:
                cnt += 1
        answer.append(cnt+1)
        
    temp = 1
    
    for i in answer:
        temp *= i
        
    return temp-1
