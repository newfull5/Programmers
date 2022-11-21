import re
import math

def _check_prime(num):
    if num < 2:
        return False
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True

def _jinbub(num, k):
    answer = ''
    
    while num > 0:
        num, d = divmod(num, k)
        answer += str(d)
        
    return answer[::-1]

def solution(n, k):
    answer = 0
    n = _jinbub(n, k)

    for num in n.split('0'):
        if not num:
            continue
            
        if _check_prime(int(num)):
            answer += 1

    return answer
