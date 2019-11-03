def solution(numbers, target):
    cnt = 0
    
    def operator(numbers, target, idx=0):
        if idx < len(numbers):
            numbers[idx] *= 1
            operator(numbers, target, idx+1)
            
            numbers[idx] *= -1
            operator(numbers, target, idx+1)
            
        elif sum(numbers) == target:
            nonlocal cnt
            cnt +=1
            
    operator(numbers, target)
    
    return cnt
