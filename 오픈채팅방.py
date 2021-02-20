def solution(record):
    diction = {}
    answer = []

    for rec in record:
        rec = rec.split()
        if rec[0] == 'Enter':
            answer.append([rec[1],"님이 들어왔습니다."])
            diction[rec[1]] = rec[2]

        elif rec[0] == 'Leave':
            answer.append([rec[1],"님이 나갔습니다."])

        else:
            diction[rec[1]] = rec[2]

    return [diction[a]+b for a,b in answer]
