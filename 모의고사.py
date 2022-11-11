'''
def solution(answers):
    man_one = [1,2,3,4,5]*2000
    man_two = [2,1,2,3,2,4,5]*1500
    man_thr = [3,3,1,1,2,2,4,4,5,5]*1000
    
    cnt_one = 0
    cnt_two = 0
    cnt_thr = 0

    for i in range(0, len(answers)):
        if man_one[i] == answers[i]:
            cnt_one += 1

    for i in range(0, len(answers)):
        if man_two[i] == answers[i]:
            cnt_two += 1

    for i in range(0, len(answers)):
        if man_thr[i] == answers[i]:
            cnt_thr += 1
            
    abc = [cnt_one, cnt_two, cnt_thr]        
            
    if cnt_one == cnt_two and cnt_two == cnt_thr:
        return [1,2,3]
    elif cnt_one == cnt_two and cnt_two > cnt_thr:
        return [1,2]
    elif cnt_two == cnt_thr and cnt_two > cnt_one:
        return [2,3]
    elif cnt_one == cnt_thr and cnt_one > cnt_two:
        return [1,3]
    else:
        return [(abc.index(max(abc)) + 1)]
'''
'''
#2020.02.16

def solution(answers):
    answers = list(map(str,answers))

    loser1 = '12345'*2000
    loser2 = '21232425'*1250
    loser3 = '3311224455'*1000
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    answers = ''.join(answers)
    
    for i in range(0, len(answers)):
        if answers[i] == loser1[i]:
            cnt1 += 1
        if answers[i] == loser2[i]:
            cnt2 += 1
        if answers[i] == loser3[i]:
            cnt3 += 1
            
    temp = sorted([[1,cnt1],[2,cnt2],[3,cnt3]], reverse = True, key = lambda abc : abc[1])
    
    if temp[0][1] == temp[1][1] == temp[2][1]:
        return [1,2,3]
    if temp[0][1] == temp[1][1]:
        return [temp[0][0],temp[1][0]]
    return [temp[0][0]]
'''
#2022.11.11
def get_score(person, answers):
    answer = 0
    for i in range(len(answers)):
        if int(person[i]) == answers[i]:
            answer += 1
    return answer

def solution(answers):
    nohoper1 = get_score('12345' * 2000, answers)
    nohoper2 = get_score('21232425' * 1250, answers)
    nohoper3 = get_score('3311224455' * 1000, answers)
    
    answer = sorted([nohoper1, nohoper2, nohoper3])
    
    if nohoper1 == nohoper2 == nohoper3:
        return [1,2,3]
    if nohoper1 > nohoper2 and nohoper1 > nohoper3:
        return [1]
    if nohoper2 > nohoper3 and nohoper2 > nohoper1:
        return [2]
    if nohoper3 > nohoper2 and nohoper3 > nohoper1:
        return [3]
    if nohoper1 == nohoper2 and nohoper2 > nohoper3:
        return [1,2]
    if nohoper1 == nohoper3 and nohoper1 > nohoper2:
        return [1,3]
    if nohoper2 == nohoper3 and nohoper2 > nohoper1:
        return [2,3]
