import re

def solution(my_string):
    return sum(map(int, re.findall('\d+', my_string)))
