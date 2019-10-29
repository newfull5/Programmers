def solution(s):
    answer = ''
    s = s.lower()
    s = s.split()
    
    for j in range(0, len(s)):
        for i in range(0,len(s[j])):
            if i % 2 == 0:
                answer += s[j][i].upper()
            else:
                answer += s[j][i]
        answer += " "
        
    return answer[:-1]
