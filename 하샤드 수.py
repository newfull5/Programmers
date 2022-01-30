'''
def solution(x):
    
    char = str(x)
    abc = 0
    
    for i in range(len(char)):
        abc = abc + int(char[i])
        
    return x % abc == 0
'''
"""
#2020.07.01
def solution(x):
    return x % sum(map(int ,list(str(x)))) == 0
"""
# 2022.01.30
def solution(x):
    return x % sum(map(int, (list(str(x))))) == 0
