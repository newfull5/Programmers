from collections import deque

def bfs(wires, wire):
    start = 1
    visited = []
    queue = deque([start])
    wires_copy = wires[:]
    wires_copy.remove(wire)
    
    while queue:
        current_node = queue.popleft()
        visited.append(current_node)
        for a,b in wires_copy:
            if a == current_node or b == current_node:
                next_node = a+b-current_node
                if next_node not in visited:
                    queue.append(next_node)
                
    return visited

def solution(n, wires):
    answer = 100_000
    for wire in wires:
        num_nodes = len(bfs(wires, wire))
        answer = min(answer, (abs(n-num_nodes - num_nodes)))
        
    return answer
