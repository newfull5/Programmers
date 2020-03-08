'''
def solution(s):
    answer = []
    
    for i in range(0, len(s)+1):
        for j in range(i+1, len(s)+1):
            temp_str = s[i:j]
            
            if temp_str == temp_str[::-1]:
                answer.append(len(temp_str))
    return max(answer)
'''
#2020.03.08
def solution(s):
    answer = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                answer.append(j-i)
    return max(answer)
