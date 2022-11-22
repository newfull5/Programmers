'''
def solution(k, dungeons):
    answer = []
    length = len(dungeons)

    def dfs(dungeon, fat, visited):
        least, cost = dungeon

        if fat < least:
            answer.append(len(visited) - 1)
            return

        if len(visited) == length:
            answer.append(len(visited))
            return

        for i in range(length):
            if i in visited:
                continue
            dfs(dungeons[i], fat-cost, visited+[i])

    for idx, dungeon in enumerate(dungeons):
        dfs(dungeon, k, [idx])

    return max(answer)
'''
#2022.11.22
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for dungeon in permutations(dungeons):
        cnt = 0
        stamina = k
        for essential, cost in dungeon:
            if stamina >= essential:
                stamina -= cost
                cnt += 1
        answer = max(answer, cnt)
    return answer
