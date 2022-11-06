def solution(s):
    stack = []
    for val in s.split():
        if val == 'Z':
            if stack:
                stack.pop()
        else:
            stack.appen(int(val))
    return sum(stack)
