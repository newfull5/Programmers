def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        a,b = divmod(i, n)
        answer.append(max(a+1, b+1))
        
    return answer
