import numpy as np

def divide(arr, length):
    return [
        arr[:length, :length],
        arr[:length, length:],
        arr[length:, :length],
        arr[length:, length:]
    ]
    
def solution(arr):
    arr = np.array(arr)
    answer = [0,0]
    
    if np.all(arr == 1):
        return [0,1]
    
    if np.all(arr == 0):
        return [1,0]
    
    lists = []
    length = len(arr) // 2
    next_queue = divide(arr, length)
    
    
    while length > 1:
        queue = next_queue[:]
        next_queue = []
        length = length // 2
        
        for li in queue:
            if np.all(li == 0):
                answer[0] += 1
                continue
                
            if np.all(li == 1):
                answer[1] += 1
                continue
                
            next_queue += divide(li, length)
            
    for num in next_queue:
        if num == 0:
            answer[0] += 1
        elif num == 1:
            answer[1] += 1
            
    return answer
