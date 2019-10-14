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
    
