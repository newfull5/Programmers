"""
def solution(num):
    cnt = 0
    while num != 1:
        cnt = cnt + 1
        if num % 2 == 1:
            num = num*3+1
        elif cnt==500:
            return -1
        else: 
            num = num/2
            
    return cnt
"""
#2022.11.12
def count_collatz(n, history, cnt):
    if n == 1:
        return cnt
    
    if n in history or cnt == 500:
        return -1

    history.append(n)
    
    if n % 2 == 0:
        return count_collatz(n//2, history, cnt+1)
    else:
        return count_collatz((n*3)+1, history, cnt+1)

def solution(num):
    return count_collatz(num, [], 0)
    
