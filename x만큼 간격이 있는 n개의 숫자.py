"""
def solution(x, n):
    abc = []
    
    for i in range(1, n+1):
        abc.append(i*x)
        
    return abc
"""
#2022.11.12 
def solution(x, n):
    if x == 0:
        return [x]*n
    return [v for v in range(x,x*(n+1),x)]
