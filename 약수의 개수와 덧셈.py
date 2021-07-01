def solution(left, right):
    
    answer = 0
    
    def divisor(n):
        answer = 1
        for i in range(1,n):
            if n % i == 0:
                answer += 1
        return answer
    
    for num in range(left,right+1):
        n = divisor(num)
        if n % 2 == 0:
            answer += num
        else:
            answer -= num
            
    return answer
