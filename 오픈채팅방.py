"""
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
"""
#2022.11.28
def solution(records):
    answer = []
    
    user_dict = {record.split()[1]:record.split()[2] for record in records if record.split()[0] != 'Leave'}
    
    for record in records:
        cmd, *user_info = record.split()
        if cmd == 'Enter':
            answer.append(f"{user_dict[user_info[0]]}님이 들어왔습니다.")
        if cmd == 'Leave':
            answer.append(f"{user_dict[user_info[0]]}님이 나갔습니다.")
            
    return answer
