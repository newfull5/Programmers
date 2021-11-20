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
