"""
#2020.03.08
from collections import defaultdict, deque

def solution(n, edge):
    val = {i:0 for i in range(1,n+1)}
    edges = defaultdict(list)
    
    for a, b in edge:
        edges[a].append(b)
        edges[b].append(a)
        
    queue = deque(edges[1])
    cnt = 1
    
    while queue:
        
        for i in range(len(queue)):
            current = queue.popleft()
            
            if val[current] == 0:
                val[current] = cnt
                for num in edges[current]:
                    queue.append(num)
        cnt += 1
        
    del val[1]
    
    maxx = max(val.values())
    answer = 0
    for i in val.values():
        if i == maxx:
            answer += 1
            
    return answer
"""
'''
def solution(n, edge):
    diction = {i:[] for i in range(1,n+1)}

    for a,b in edge:
        diction[a].append(b)
        diction[b].append(a)

    start = set([1])

    visited = set(start)

    next = set([])

    while True:
        for num in start:
            next.update(set(diction[num]))

        next = next - visited

        visited = visited | next

        if not next:
            return len(start)

        start = next.copy()
'''
from collections import deque

def solution(n, vertex):
    visited = [1]
    queue = deque([[1,1]])
    answer = []
    
    while queue:
        start_node, cost = queue.popleft()
        answer.append([start_node, cost])
        
        for node1, node2 in vertex:
            if node1 in visited and node2 in visited:
                continue
                
            if start_node in [node1, node2]:
                new_node = node1+node2-start_node
                queue.append([new_node, cost+1])
                visited.append(new_node)
                
    max_cost = answer[-1][-1]
    answer = [node for node, cost in answer if cost == max_cost]
    
    return len(answer)
