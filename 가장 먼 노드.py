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
