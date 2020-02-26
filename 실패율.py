'''
def solution(N, stages):
    length = len(stages)
    arr = []
    answer = []

    for i in range(1,N+1):
        if length == 0:
            arr.append((i,0))
            continue
        arr.append((i,stages.count(i)/length))
        length = length - stages.count(i)


    arr = sorted(arr, key=lambda arr: arr[1], reverse = True)

    for i in range(0, len(arr)):
        answer.append(arr[i][0])
        
    return answer
'''

#2020.02.26
def solution(N, stages):
    stages.sort()
    stack = []
    failrate = []
    answer = []
    
    for num in set(stages):
        stack.append([num,stages.count(num)])
        
    right = len(stages)
    left = 0
    
    for num in stack:
        right = right - left
        left = num[-1]
        failrate.append([num[0], left/right])
        
    for num in sorted(failrate, key = lambda a: a[-1], reverse = True):
        answer.append(num[0])
    
    for i in range(1, N+1):
        if N+1 in answer:
            answer.remove(N+1)
        if not i in answer:
            answer.append(i)
            
    return answer
