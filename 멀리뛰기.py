"""
from math import factorial

def solution(n):
    answer = 0
    for i in range(0, (n//2)+1):
        answer += factorial(n-i)//(factorial(i)*factorial(n-(i*2)))
    return answer % 1234567
"""
#2022.11.15
from math import factorial

def combination(a,b):
    if a == 0 or b == 0:
        return 1
    return factorial(a+b) // (factorial(a)*factorial(b))

def solution(n):
    answer = 0
    arr = divmod(n, 2)

    for v in range(arr[0]+1):
        answer += combination(arr[0]-v, arr[1]+(v*2)) % 1234567
        
    return answer % 1234567
