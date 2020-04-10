def solution(s):
    s = s[2:-2].replace('{','')
    s = sorted(s.split('},'), key = lambda x : len(x))
    s = list(map(lambda x: set(x.split(',')),s)) 
    answer = []
    
    answer.append(list(s[0])[0])
    for i in range(1, len(s)):
        answer.append(list(s[i] - s[i-1])[0])
        
    return list(map(int,answer))
