'''
def solution(array, commands):
    answer = []
    arr = [] 
    
    for t in range(0, len(commands)):
        i = commands[t][0]
        j = commands[t][1]
        k = commands[t][2] 

        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])

    return answer
'''
'''
#2020.04.04
def solution(array, commands):
    answer = []
    for arr in commands:
        answer.append(sorted(array[arr[0]-1:arr[1]])[arr[2]-1])
        
    return answer
'''
"""
#2020.05.28
#뭔가 짠하다... 내가 점점 달라졌구나 싶다.
def solution(array, commands):
    return [(sorted(array[i-1:j])[k-1]) for i,j,k in commands]
"""
'''
#2020.12.24
def solution(array, commands):
    answer = []
    for command in commands:
        a,b,c = command
        answer.append(sorted(array[a-1:b])[c-1])
        
    return answer
'''
#2021.06.23
def solution(array, commands):
    return [sorted(array[a-1:b])[c-1] for a,b,c in commands]
