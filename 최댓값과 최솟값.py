def solution(s):
    answer = []
    
    a = s.split()
    
    for lis in a:
        answer.append(int(lis))
        
    answer.sort()
    
    k = "{} {}".format(answer[0],answer[-1])
    
    return k
