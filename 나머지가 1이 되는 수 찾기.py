"""
def soinsu_boonhae(num):
    for i in range(2, num):
        if num % i == 0:
            return i
    return num

def solution(n):
    num = n-1
    while True:
        if num == soinsu_boonhae(num):
            return num
        num = soinsu_boonhae(num)
"""
#2022.11.08

def solution(n):
    for num in range(1, n):
        if n % num == 1:
            return num
