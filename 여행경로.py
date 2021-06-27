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
