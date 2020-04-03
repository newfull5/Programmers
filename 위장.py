'''
def solution(clothes):
    kind = []
    answer = []
    temp = ''
    
    for arr in clothes:
        if temp != arr[-1]:
            temp = arr[-1]
            kind.append(temp)
            
    kind = list(set(kind))
    
    for i in range(0,len(kind)):
        cnt = 0
        for arr in clothes:
            if arr[-1] == kind[i]:
                cnt += 1
        answer.append(cnt+1)
        
    temp = 1
    
    for i in answer:
        temp *= i
        
    return temp-1
'''

'''
# 2020.02.25
def solution(clothes):
    kind = []
    cnt = []
    answer = 1
    
    for clothe in clothes:
        kind.append(clothe[1])
    
    for kin in set(kind):
        cnt.append(kind.count(kin)+1)    
    
    for num in cnt:
        answer *= num
        
    return answer-1
'''

#2020.04.03
from collections import Counter
from functools import reduce

def solution(clothes):
    
    val = Counter([category for kind, category in clothes])
    val = list(val.values())
    
    for i in range(0, len(val)):
        val[i] = val[i]+1
        
    return reduce(lambda x,y: x*y,val)-1
