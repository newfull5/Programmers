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
