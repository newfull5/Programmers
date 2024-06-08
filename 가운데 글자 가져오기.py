"""
def solution(s):
    if len(s) % 2 == 1:
        return s[(len(s)//2)]
    else: 
        return s[(len(s)//2)-1:(len(s)//2)+1]
"""
#2022.11.13
def solution(s):
    if len(s) % 2 == 0:
        return s[(len(s)//2)-1:(len(s)//2)+1]
    return s[len(s)//2]
