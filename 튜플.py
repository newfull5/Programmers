'''
import re

def solution(s):
    s = s.split('},')

    q = re.compile('\d+')
    arr = ([set(q.findall(arr)) for arr in s])
    arr = sorted(arr, key=lambda x: len(x))

    answer_set = set()
    answer = []

    for a in arr:
        answer.append(int(list(a - answer_set)[0]))
        answer_set = a

    return answer
'''
#2022.11.16
import re

def solution(s):
    s = sorted([v.split(',') for v in re.findall('\{((?:\d[,]?)+)\}',s)], key = lambda x: len(x))
    
    answer = s.pop(0)
    
    for arr in s:
        answer += list(set(arr) - set(answer))
        
    return [int(v) for v in answer]
