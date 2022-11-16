'''
def solution(s):
    def check(s):
        stack = []

        while s:
            stack.append(s.pop(0))

            while True:
                if len(stack) >= 2:
                    if stack[-1] == ']' and stack[-2] == '[':
                        stack.pop()
                        stack.pop()
                        continue

                    if stack[-1] == ')' and stack[-2] == '(':
                        stack.pop()
                        stack.pop()
                        continue

                    if stack[-1] == '}' and stack[-2] == '{':
                        stack.pop()
                        stack.pop()
                        continue

                break

        if not stack:
            return True
        return False
    
    s = list(s)
    answer = 0
    
    for _ in range(len(s)):
        s.append(s.pop(0))
        if check(s[:]):
            answer += 1
            
    return answer
'''
#2022.11.16
from collections import deque

def check_bracket(s):
    s = ''.join(list(s))
    
    for _ in range(len(s)//2):
        s_copy = s[:]
        s = s.replace('()','')
        s = s.replace('{}','')
        s = s.replace('[]','')
        if not s:
            return True
        if s == s_copy:
            return False

def solution(s):
    s = deque(s)
    answer = 0
    
    for _ in range(len(s)):
        s.append(s.popleft())
        if check_bracket(list(s)):
            answer += 1
            
    return answer
