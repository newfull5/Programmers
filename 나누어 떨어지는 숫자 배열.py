def solution(arr, divisor):
    answer = []
    
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
        
    if not answer:
        return [-1]
    else:
        return sorted(answer)
