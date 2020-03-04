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


