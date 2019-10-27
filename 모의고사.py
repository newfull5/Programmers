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
