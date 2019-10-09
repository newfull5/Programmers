def solution(s):
    arr = []
    arr.append(s[0])
    
    for i in s:
        if arr[-1] != i:
            arr.append(i)
            
    return arr
