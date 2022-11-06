import re

def solution(my_string):
    return sorted([int(val) for val in re.findall('\d', my_string)])
