'''
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
'''
#2020.02.29

def solution(s):
    s = s.lower()
    new_list = s.split(' ')
    answer = ''
    for char in new_list:
        for i in range(0, len(char)):
            if i % 2 == 0:
                answer += char[i].upper()
            else:
                answer += char[i]
        answer += ' '
    return answer[:-1]
                

