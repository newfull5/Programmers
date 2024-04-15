from collections import deque

def solution(N, roads, K):
    diction = {i: 1_000_000 for i in range(1, N+1)}
    diction[1] = 0
    queue = deque([1])
    visited = []
    
    while queue:
        current_node = queue.popleft()
        near_node = []
        
        for node1, node2, cost in roads:
            if current_node in [node1, node2]:
                near_node.append([node1,node2,cost])

        for node1, node2, cost in near_node:
            next_node = node1+node2-current_node
            diction[next_node] = min(diction[current_node] + cost, diction[next_node])
            if next_node not in visited:
                queue.append(next_node)
        
        visited.append(current_node)
    
    return len([val for val in diction.values() if val <= K])
