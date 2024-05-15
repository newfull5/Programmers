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
'''
from heapq import heappush, heappop

def solution(operations):
    length = 0
    min_heap = []
    max_heap = []
    
    for operation in operations:
        oper, num = operation.split()
        if oper == 'I':
            heappush(min_heap, int(num))
            heappush(max_heap, int(num)*-1)
            length += 1
            
        elif operation == 'D 1' and length != 0:
            heappop(max_heap)
            min_heap.pop()
            length -= 1
            
        elif operation == 'D -1' and length != 0:
            heappop(min_heap)
            max_heap.pop()
            length -= 1
        
    if length == 0:
        return [0,0]
    
    return [max_heap[0]*-1, min_heap[0]]
