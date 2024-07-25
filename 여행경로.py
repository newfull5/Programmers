'''
def solution(tickets):
    
    answer = []
    
    def DFS(visited, rest):

        if not rest:
            answer.append(visited)
            return

        current = visited[-1]

        for a,b in rest:
            if a == current:
                temp = rest[:]
                temp.remove([a,b])
                DFS(visited + [b], temp)
                
    DFS(['ICN'],tickets)

    return sorted(answer)[0]
'''
def solution(tickets):
    answer = []
    result = []
    
    def dfs(start, visited):
        if len(visited) == len(tickets):
            answer.append(visited)
            return
        
        possible_distination = []
        for start_node, desti_node in tickets:
            if start_node != start:
                continue
                
            if [start_node, desti_node] in visited:
                continue
                
            possible_distination.append(desti_node)
            
        
        for next_node in possible_distination:
            dfs(next_node, visited + [[start, next_node]])
            
    dfs("ICN", [])
    
    for li in answer:
        result.append(["ICN"] + [b for a,b in li])
    
    return sorted(result)[0]
