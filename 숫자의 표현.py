"""
def solution(n):
    answer = []
    for i in range(1,n):
        temp = 0
        for j in range(i,n):
            temp += j
            if temp == n:
                answer.append(j-i)
            if temp > n:
                break
                
    return len(answer)+1
"""
'''
#2022.11.14
def search_maxn(n):
    for i in range(1, 140):
        if i*(i+1)/2 > n:
            return i-1

def solution(n):
    max_n = search_maxn(n)
    answer = 1
    
    for i in range(2, max_n+1):
        for j in range(10000):
            if sum(range(1+j, 1+j+i)) == n:
                answer += 1
                break
            if sum(range(1+j, 1+j+i)) > n:
                break
                
    return answer
'''
def check_max_num(n):
    sum_ = 0
    for i in range(0, n+1):
        sum_ += i
        if sum_ >= n:
            return i
        
def solution(n):
    answer = 0
    reps = check_max_num(n)
    
    while reps > 0:
        for idx in range(1, n):
            sum_ = sum(list(range(idx, reps+idx)))
            
            if sum_ == n:
                answer += 1
                break
            
            if sum_ > n:
                break
                
        reps -= 1
        
    return answer+1
