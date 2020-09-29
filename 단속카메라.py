def solution(routes):
    routes = sorted(routes, key = lambda x: x[-1])
    length = len(routes)
    chk = [False] * length
    answer = 0

    for i in range(length):
        if chk[i]:
            continue

        camera = routes[i][-1]
        answer += 1

        for j in range(i, length):
            if routes[j][0] <= camera and camera <= routes[j][1]:
                chk[j] = True
    return answer
