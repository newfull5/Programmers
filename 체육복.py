def solution(n, lost, reserve):
    for i in range(0, len(lost)):
        for j in range(0, len(reserve)):
            if lost[i] == reserve[j]:
                lost[i] = 0
                reserve[j] = 0
            elif lost[i]-1 == reserve[j]:
                lost[i] = 0
                reserve[j] = 0
            elif lost[i]+1 == reserve[j]:
                lost[i] = 0
                reserve[j] = 0     

    lost = list(set(lost))
    reserve = list(set(reserve))
    lost.remove(0)
    reserve.remove(0)
    
    return n-len(lost)
