'''
def solution(n):
    a = bin(n)
    
    while True:
        n += 1
        if a.count('1') == bin(n).count('1'):
            break
            
    return n
'''
#2022.11.14
def solution(n):
    num_one = bin(n).count('1')
    for num in range(n+1, 1000000):
        if bin(num).count('1') == num_one:
            return num
        
