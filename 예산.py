"""
def solution(d, budget):
    
    d.sort()
    cnt=0
    
    for i in d:
        if budget>=i:
            budget = budget-i
            cnt = cnt + 1
    
    return cnt
"""

#2022.11.12
def solution(d, budget):
    d.sort()
    for idx in range(len(d)):
        if budget < d[idx]:
            return idx
        budget -= d[idx]
    return len(d)
