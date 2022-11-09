"""
def solution(a, b):
    return sum(map(lambda x:x[0]*x[1], tuple(zip(a,b))))
"""
#2022.11.09
def solution(a, b):
    return sum(val1*val2 for val1, val2 in zip(a,b))
