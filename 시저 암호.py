"""
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
"""
#2022.11.12
import re

def shift_char(char, n):
    if char.islower() and ord(char) + n > ord('z'):
        return chr(ord(char) + n - 26)
    if char.isupper() and ord(char) + n > ord('Z'):
        return chr(ord(char) + n - 26)
    return chr(ord(char) + n)
    
def solution(s, n):
    answer = ''
    
    for char in s:
        if re.search('[a-zA-z]', char):
            answer += shift_char(char, n)
        else:
            answer += ' '
            
    return answer
