'''
def solution(n):
    fibo = [0,0,1,2]
    
    for i in range(4,n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
        
    return ( fibo[-1] % 1234567 )
'''
#2022.11.14
def solution(n):
    fibo = [0,1]
    
    for i in range(2,n+1):
        fibo.append(fibo[-1] + fibo[-2])
        
    return fibo[-1] % 1234567
