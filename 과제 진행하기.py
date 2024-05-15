def trans_time(string):
    a,b = string.split(':')
    return int(b) + int(a) * 60


def make_plan(plan):
    task, time, cost = plan
    return [task, trans_time(time), int(cost)]


def solution(plans):
    answer = []
    stack = []
    current_time = 0
    current_task = ''
    plans = sorted([make_plan(plan) for plan in plans], key=lambda x: x[1])
    
    for i in range(len(plans)-1):
        task1, time1, cost1 = plans[i]
        task2, time2, cost2 = plans[i+1]
        
        if i == 0:
            current_task = task1
            current_time = time1
            
        if current_time+int(cost1) > time2:
            stack.append([task1, cost1 - (time2-time1)])
            current_time = time2
            
        else:
            answer.append(task1)
            current_time = time2
            
    else:
        answer.append(plans[-1][0])
        
    while stack:
        answer += [stack.pop()[0]]
        
    return answer
