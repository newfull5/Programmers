'''
def solution(s):
    s = s.lower()
    s = s.replace(s[0],s[0].upper(),1)
   
    for i in range(1,len(s)-1):
        if s[i] == ' ':
            s = s.replace(s[i+1],s[i+1].upper(),1)

    return s
     
    이게 안되는 이유를 모르겠다
    
'''
 
def solution(s):
    s = s.lower()
    answer = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i]
    return answer
