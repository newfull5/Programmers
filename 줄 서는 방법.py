from math import factorial as F

def solution(n, k):
    arr = list(range(1,n+1))

    answer = []

    while n != 0:
        answer.append(arr.pop((k-1) // F(n-1)))
        k %= F(n-1)
        n -= 1
        
    return answer
