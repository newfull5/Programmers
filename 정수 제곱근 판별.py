"""
def solution(n):

    for i in range(10000001):
        if i*i == n:
            return (i+1)*(i+1)

    return -1
"""
#2022.11.12
def solution(n):
    if n ** (1/2) == int(n ** (1/2)):
        return (n**(1/2) +1)**2
    return -1
