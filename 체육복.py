'''
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
'''
'''
#2020.05.27
def solution(n, lost, reserve):
    
    for res in reserve[:]:
        if res in lost:
            lost.remove(res)
            reserve.remove(res)
            
    for res in reserve:
        if res-1 in lost:
            lost.remove(res-1)
        elif res+1 in lost:
            lost.remove(res+1)
            
    return n-len(lost)
'''
'''
#2020.10.17
def solution(n, lost, reserve):
    lost_copy = lost[:]

    for los in lost_copy:
        if los in reserve:
            reserve.remove(los)
            lost.remove(los)

    for res in reserve:
        if res-1 in lost:
            lost.remove(res-1)
        elif res+1 in lost:
            lost.remove(res+1)

    return (n - len(lost))
'''
#2022.11.11
def run_ltr(n, lost, reserve):
    for student in (set(lost) & set(reserve)):
        lost.remove(student)
        reserve.remove(student)
    
    for res in reserve:
        if res-1 in lost:
            lost.remove(res-1)
        elif res+1 in lost:
            lost.remove(res+1)
            
    return n-len(lost)    
    
def run_rtl(n, lost, reserve):
    for student in (set(lost) & set(reserve)):
        lost.remove(student)
        reserve.remove(student)
        
    for res in reserve:
        if res+1 in lost:
            lost.remove(res+1)
        elif res-1 in lost:
            lost.remove(res-1)
            
    return n-len(lost)  

def solution(n, lost, reserve):
    return max(run_rtl(n,lost[:],reserve[:]), run_ltr(n,lost[:],reserve[:]))
