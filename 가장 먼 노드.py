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
