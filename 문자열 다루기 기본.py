"""
def solution(s):
    return s.isnumeric()
"""
#2022.11.12
import re

def solution(s):
    if len(s) == 4 or len(s) == 6:
        if re.search('[a-zA-Z]', s):
            return False
        return True
    return False
