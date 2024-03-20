def convert_datetime(date_list):
    y,m,d = date_list
    m += y * 12
    d += m * 28
    return d

def solution(today, terms, privacies):
    answer = []
    today = convert_datetime(map(int, today.split('.')))
    diction = {term.split()[0]:int(term.split()[-1]) for term in terms}
    
    for idx, privacy in enumerate(privacies):
        date, typ = privacy.split()
        date = convert_datetime(map(int, date.split('.'))) + diction[typ] * 28
        if date <= today:
            answer.append(idx+1)
            
    return answer
