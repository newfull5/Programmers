'''
def solution(s):
    stack = []
    
    if s[-1] == '(':
        return False
    
    for i in list(s):
        if len(stack) == 0:
            stack.append(i)
            if i==')':
                return False
            
        elif stack[-1] != i:
            del stack[-1]
            
        else:
            if i==')':
                return False
            stack.append(i)


    return len(stack) == 0


'''
'''
#2020.02.14

def solution(s):
    answer = s[0]
    for i in range(1, len(s)):
        if s[i] == ')':
            answer = answer[:-1]
        else:
            answer += s[i]
    return answer == ''
    
'''
#2022.11.13
from collections import deque

def solution(s):
    s = deque(list(s))
    stack = [0]
    
    while s:
        bracket = s.popleft()
        if bracket == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(bracket)
            
    if stack == [0]:
        return True
    return False
