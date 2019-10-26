def solution(n, lost, reserve):
    intersec = list(set(lost) & set(reserve))
    lost = list(set(lost) - set(intersec))
    reverse = list(set(lost) - set(intersec))
    
    for i in range(0, n):
        if i in lost:
            if i-1 in reserve:
                reserve.remove(i-1)
                lost.remove(i)
            elif i+1 in reserve:
                reserve.remove(i+1)
                lost.remove(i)
                
    return n - len(lost)
