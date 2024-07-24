'''
def solution(n, costs):
    costs = sorted(costs, key = lambda x: x[-1])

    connected = set([costs[0][0]])

    answer = 0

    while len(connected) != n:
        for a,b,c in costs:

            if a in connected and b in connected:
                continue

            if a in connected or b in connected:

                connected.update([a,b])

                answer += c
                break

    return answer
'''
def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[-1])
    visited = set([costs[0][0]])
    
    while len(visited) != n:
        for node1, node2, cost in costs:
            if node1 in visited and node2 in visited:
                continue
            if node1 in visited or node2 in visited:
                visited.update([node1, node2])
                answer += cost
                break
                
    return answer
