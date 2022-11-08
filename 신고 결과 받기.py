def solution(id_list, report, k):
    report = list(set(report))
    
    diction = {}
    for user in id_list:
        diction[user] = 0
    
    for rpt in report:
        _, reported_user = rpt.split()
        diction[reported_user] += 1
        
    banned = [name for name, score in diction.items() if score >= k]
    
    answer = {}
    for user in id_list:
        answer[user] = 0
        
    for rpt in report:
        reporting_user, reported_user = rpt.split()
        if reported_user in banned:
            answer[reporting_user] += 1
        
    return list(answer.values())
