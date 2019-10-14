def solution(n):
    a = bin(n)
    
    while True:
        n += 1
        if a.count('1') == bin(n).count('1'):
            break
            
    return n
