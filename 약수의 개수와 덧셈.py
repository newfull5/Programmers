"""
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
"""
#2022.11.08
def get_denonum(number):
    answer = 0
    for num in range(1, number+1):
        if number % num == 0:
            answer += 1
    return answer

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        denominator_num = get_denonum(num)
        if denominator_num % 2 == 0:
            answer += num
        else:
            answer -= num
            
    return answer
