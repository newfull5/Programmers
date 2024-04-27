import numpy as np

def make_queue(r1,c1,r2,c2):
    queue = []
    for c in range(c1, c2):
        queue.append([r1-1,c-1])
    for r in range(r1-1, r2-1):
        queue.append([r-1, c2-1])
    for c in range(c2, c1, -1):
        queue.append([r2-1, c-1])
    for r in range(r2, r1, -1):
        queue.append([r-1, c1-1])
    return queue

def solution(rows, columns, queries):
    arr = np.array(range(1, columns*rows+1)).reshape(rows,columns)
    
    a,b,c,d = queries[1]
    queue = make_queue(a,b,c,d)
    ready_queue = queue[:]
    ready_queue = ready_queue + [ready_queue.pop(0)]
    
    for node, next_node in zip(queue, ready_queue):
        next_element = arr[next_node[0], next_node[1]]
        current_element = arr[node[0], node[1]]
        
        print(next_element, current_element)
