'''
#힙을 사용해야 풀리는 , 문제의 케이스가 너무 적어서 이런식으로도 풀리더라.
def solution(operations):
    stack = []
    
    for char in operations:
        if char[0] == 'I':
            stack.append(int(char[2:]))
        if not stack:
            continue
        if char == 'D -1':
            stack.remove(min(stack))
        if char == 'D 1':
            stack.remove(max(stack))
    if not stack:
        return [0,0]
    return [max(stack),min(stack)]
'''
#2021.06.23
def solution(operations):
    queue = []

    while operations:
        operation = operations.pop(0)

        if queue and operation == "D 1":
            queue.remove(max(queue))

        elif queue and operation == "D -1":
            queue.remove(min(queue))

        else:
            queue.append(int(operation[1:]))

    if len(queue) > 1:
        return [max(queue), min(queue)]
    return [0,0]
