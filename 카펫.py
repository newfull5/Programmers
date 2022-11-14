'''
def solution(brown, red):
    brown = brown - 4
    brown = brown // 2
    temp = []
    for i in range(1, brown):
        if i * (brown - i) == red:
            return [(brown-i)+2,i+2]
'''
"""
#2020.03.01
def solution(brown, red):
    enffp = (brown - 4)//2
    for i in range(enffp):
        if (i * (enffp - i)) == red:
            return [(enffp-i)+2,i+2]
"""
"""
#2021.07.07
def solution(brown, yellow):
    brown -= 4
    brown //= 2

    for i in range(1, brown//2 +1):
        if ((brown-i) * i) == yellow:
            return [brown-i + 2, i + 2]
"""
#2022.11.14
def solution(brown, yellow):
    brown = (brown-4)//2
    # brown = 20
    
    for n in range(1, yellow+1):
        if n + (yellow/n) == brown:
            return [yellow//n+2, n+2]
