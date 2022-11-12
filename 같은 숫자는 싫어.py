"""
def solution(s):
    arr = []
    arr.append(s[0])
    
    for i in s:
        if arr[-1] != i:
            arr.append(i)
            
    return arr
"""
#2022.11.13
def solution(arr):
    answer = [-100]
    for val in arr:
        if val == answer[-1]:
            continue
        answer.append(val)
    return answer[1:]
