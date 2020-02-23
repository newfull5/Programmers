'''
2020.02.23
def solution(skill, skill_trees):
    right = []
    stack = []
    cnt = 0
    
    for i in range(0, len(skill)+1):
        right.append(skill[:i])
        
    skill = list(skill)    
    
    for each in skill_trees:
        string = ''
        for i in range(0,len(each)):
            if each[i] in skill:
                string += each[i]
                
        stack.append(string)
        
    for num in stack:
        if num in right:
            cnt += 1
            
    return cnt
'''
def solution(skill, skill_trees):
    answer = []
    for i in range(0, len(skill)):
        answer.append(skill[:i])
    answer.append(skill)

    cnt = 0
    for arr in skill_trees:
        temp = []
        for i in range(0,len(arr)):
            if arr[i] in list(skill):
                temp.append(arr[i])
                print(temp)
        if ''.join(temp) in answer:
            cnt += 1
            
    return cnt
