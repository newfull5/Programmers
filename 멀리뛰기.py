from math import factorial

def solution(n):
    answer = 0
    for i in range(0, (n//2)+1):
        answer += factorial(n-i)//(factorial(i)*factorial(n-(i*2)))
    return answer % 1234567
