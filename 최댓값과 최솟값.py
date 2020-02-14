def solution(s):
    answer = []
    
    a = s.split()
    
    for lis in a:
        answer.append(int(lis))
        
    answer.sort()
    
    k = "{} {}".format(answer[0],answer[-1])
    
    return k

--------------------
2020.02.14

def solution(s):
    temp = s.split()
    temp = list(map(int,temp))
    
    return '{} {}'.format(min(temp),max(temp))
