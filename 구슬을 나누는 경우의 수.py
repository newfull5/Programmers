from math import factorial as fac

def combination(n, c):
    return fac(n) / (fac(c) * fac(n-c))
    
def solution(balls, share):
    return combination(balls, share)
