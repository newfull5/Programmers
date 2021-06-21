'''
#2019.10.27
def solution(progresses, speeds):
    days = []
    for i in range(0, len(progresses)):
        days.append(0)

    for i in range(0, len(progresses)):
        while progresses[i] < 100:
            progresses[i] = progresses[i] + speeds[i]
            days[i] += 1

    answer = []
    answerr= []

    first = 0

    for i in range(0, len(days)):
        if first < days[i]:
            answer.append(days[:i])
            first = days[i]

    for i in range(0, len(answer)-1):
        answerr.append(len(answer[i+1]) - len(answer[i]))

    answerr.append(len(days) - len(answer[-1]))

    return answerr
'''
'''
#2020.02.23
import math

def solution(progresses, speeds):
    stack = []
    answer = []
    
    for i in range(0, len(speeds)):
        stack.append(math.ceil((100 - progresses[i])/speeds[i]))

    pin = 0
    for i in range(0, len(stack)):
        if stack[i] > stack[pin]:
            answer.append(i - pin)
            pin = i
            
    answer.append(len(stack) - pin)
    
    return answer

'''
"""
#2020.04.05
#코드가 점점 간결해진다. 처음 풀이와 비교해 보면 꽤 많이 성장한 것같다.
import math

def solution(progresses, speeds):
    arr = [math.ceil(a/b) for a,b in zip(list(map(lambda x: 100-x,progresses)),speeds)]    
    answer = []
    pin = 0
    
    for i in range(0, len(arr)):
        if arr[i] > arr[pin]:
            answer.append(i - pin)
            pin = i

    answer.append(len(arr) - pin)
    
    return answer
"""
#2020.06.21

import math
    
def solution(progresses, speeds):

    stack = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    answer = []

    num = stack.pop(0)
    cnt = 1
    while stack:
        if num < stack[0]:
            num = stack.pop(0)
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
            stack.pop(0)

    answer.append(cnt)

    return answer
