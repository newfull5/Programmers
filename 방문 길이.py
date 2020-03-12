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
