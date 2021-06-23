"""
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
"""
#2021.06.24
def solution(numbers, target):
    
    answer = 0
    
    def DFS(num,idx):

        nonlocal answer

        if idx == len(numbers):
            if num == target:
                answer += 1
            return
        
        DFS(num + numbers[idx], idx+1)

        DFS(num - numbers[idx], idx+1)
        
    DFS(0, 0)
    return answer
