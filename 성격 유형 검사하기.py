def solution(surveys, choices):
    answer = ''
    diction = {
        'RT': 0,
        'CF': 0,
        'JM': 0,
        'AN': 0
    }
    
    for survey, choice in zip(surveys, choices):
        if survey == 'RT':
            diction['RT'] += (choice-4)
        if survey == 'TR':
            diction['RT'] += (choice-4)*-1
        if survey == 'CF':
            diction['CF'] += (choice-4)
        if survey == 'FC':
            diction['CF'] += (choice-4)*-1
        if survey == 'JM':
            diction['JM'] += (choice-4)
        if survey == 'MJ':
            diction['JM'] += (choice-4)*-1
        if survey == 'AN':
            diction['AN'] += (choice-4)
        if survey == 'NA':
            diction['AN'] += (choice-4)*-1
            
    if diction['RT'] <= 0:
        answer += 'R'
    else:
        answer += 'T'
    if diction['CF'] <= 0:
        answer += 'C'
    else:
        answer += 'F'
    if diction['JM'] <= 0:
        answer += 'J'
    else:
        answer += 'M'
    if diction['AN'] <= 0:
        answer += 'A'
    else:
        answer += 'N'
    return answer
