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
