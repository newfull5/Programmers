'''def solution(s):
    answer = []
    
    a = s.split()
    
    for lis in a:
        answer.append(int(lis))
        
    answer.sort()
    
    k = "{} {}".format(answer[0],answer[-1])
    
    return k
'''
'''
#2020.02.14

def solution(s):
    temp = s.split()
    temp = list(map(int,temp))
    
    return '{} {}'.format(min(temp),max(temp))
'''
#2022.11.13
def solution(s):
    s = [int(v) for v in s.split()]
    return f"{min(s)} {max(s)}"
