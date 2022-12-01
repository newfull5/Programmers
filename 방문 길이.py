"""
def solution(dirs):
    player = [0,0]
    answer = [[0,0]]
    answers = []
    
    for i in range(0, len(dirs)):
        if dirs[i] == 'U':
            if player[1] < 5:
                player[1] += 1
        elif dirs[i] == 'L':
            if player[0] > -5:
                player[0] -= 1
        elif dirs[i] == 'D':
            if player[1] > -5:
                player[1] -= 1
        elif dirs[i] == 'R':
            if player[0] < 5:
                player[0] += 1
        answer.append(player[:])

    for i in range(0, len(answer)-1):
        if answer[i] != answer[i+1]:
            if answer[i]+answer[i+1] not in answers and answer[i+1]+answer[i] not in answers:
                answers.append(answer[i]+answer[i+1])
        
    return len(set(map(str,answers)))
"""
#2022.12.01
def solution(dirs):
    visited = set() # [(start_x, start_y, end_x, end_y), ...]
    
    start_x = 0
    start_y = 0
    for direc in dirs:
        if direc == 'U' and start_y != 5:
            visited.add((start_x, start_y, start_x, start_y+1))
            visited.add((start_x, start_y+1, start_x, start_y))
            start_y += 1
        elif direc == 'D' and start_y != -5:
            visited.add((start_x, start_y, start_x, start_y-1))
            visited.add((start_x, start_y-1, start_x, start_y))
            start_y -= 1
        elif direc == 'L' and start_x != -5:
            visited.add((start_x, start_y, start_x-1, start_y))
            visited.add((start_x-1, start_y, start_x, start_y))
            start_x -= 1
        elif direc == 'R' and start_x != 5:
            visited.add((start_x, start_y, start_x+1, start_y))
            visited.add((start_x+1, start_y, start_x, start_y))
            start_x += 1
            
    return len(visited)//2
