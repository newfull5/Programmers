import re

def mult(expression):
    
    stack = []
    
    for exp in expression:
        if not stack:
            stack.append(exp)
            continue

        if stack[-1] == '*':
            stack.pop()
            stack.append(int(stack.pop()) * int(exp))
            continue

        stack.append(exp)
        
    return stack

def plus(expression):
    
    stack = []
    
    for exp in expression:
        if not stack:
            stack.append(exp)
            continue

        if stack[-1] == '+':
            stack.pop()
            stack.append(int(stack.pop()) + int(exp))
            continue

        stack.append(exp)
    
    return stack

def minus(expression):
    
    stack = []
    
    for exp in expression:
        if not stack:
            stack.append(exp)
            continue

        if stack[-1] == '-':
            stack.pop()
            stack.append(int(stack.pop()) - int(exp))
            continue

        stack.append(exp)
    return stack

def solution(expression): 
    q = re.compile('\d+|[*]|[-]|[+]')
    expression = q.findall(expression)
    
    return max([
        abs(minus(plus(mult(expression)))[0]), # * > + > -
        abs(minus(mult(plus(expression)))[0]), # + > * > -
        abs(plus(minus(mult(expression)))[0]), # * > - > +
        abs(mult(plus(minus(expression)))[0]), # - > + > *
        abs(plus(mult(minus(expression)))[0]), # - > * > +
        abs(mult(minus(plus(expression)))[0])  # + > - > *
    ])
 
 
