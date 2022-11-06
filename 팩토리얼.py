import math

def solution(n):
    for num in range(1,11):
        if n < math.factorial(num):
            return num-1
    return 10
