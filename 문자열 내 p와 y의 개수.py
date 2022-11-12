"""
def solution(s):
    return s.upper().count('P') == s.upper().count('Y')
"""
#2022.11.13
def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')
