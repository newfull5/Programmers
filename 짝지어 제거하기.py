'''
def solution(s):
    result = []
    for i in s:
        if not result:
            result.append(i)
        elif result[-1] == i:
            result.pop()
        else:
            result.append(i)
    return int(not bool(result))
'''
'''
#2020.03.04
import collections

def solution(s):
    s = list(s)
    while True:
        length = len(s)
        stack = collections.deque([])
        if not stack and not s:
            return 1
        for num in s:
            if len(stack) == 0:
                stack.append(num)
                continue
            if num == stack[-1]:
                stack.pop()
            else:
                stack.append(num)
        s = list(stack)
        if length == len(s):
            return 0
'''
'''
#2020.07.02
def solution(s):
    stack = []
    
    if len(s) % 2 == 1:
        return 0
    for a in list(s):
        stack.append(a)
        try:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        except IndexError:
            continue           
    if not stack:
        return 1
    return 0
'''
#2022.11.14
from collections import deque

def solution(s):
    s = deque(s)
    stack = [0]
    
    while s:
        temp = s.popleft()
        if temp == stack[-1]:
            stack.pop()
        else:
            stack.append(temp)
            
    if stack == [0]:
        return 1
    return 0
