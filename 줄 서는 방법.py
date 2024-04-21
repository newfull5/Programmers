'''
from math import factorial as F

def solution(n, k):
    arr = list(range(1,n+1))

    answer = []

    while n != 0:
        answer.append(arr.pop((k-1) // F(n-1)))
        k %= F(n-1)
        n -= 1
        
    return answer
'''    
from math import factorial as fac

def solution(n, k):
    arr = [i for i in range(1, n + 1)]
    answer = []
    
    while arr:
        a = (k - 1) // fac(n - 1)
        answer.append(arr.pop(a))
        
        k = k % fac(n - 1)
        n -= 1
        
    return answer
