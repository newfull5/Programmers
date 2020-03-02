'''
def solution(n):
    cnt = 1
    
    while True:
        if n == 1:
            return cnt
        elif n% 2 == 1:
            n = n-1
            cnt = cnt + 1
        else:
            n = n/2
'''
#2020.03.02
def solution(n):
    cnt = 1
    while n > 1:
        if n % 2 == 0:
            n = n//2
            continue
        else:
            n = n//2
            cnt += 1
    return cnt
