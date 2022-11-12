"""
def solution(arr, divisor):
    answer = []
    
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
        
    if not answer:
        return [-1]
    else:
        return sorted(answer)
"""
#2022.11.13
def solution(arr, divisor):
    answer = []
    
    for val in sorted(arr):
        if val % divisor == 0:
            answer.append(val)
            
    if not answer:
        return [-1]
    return answer
