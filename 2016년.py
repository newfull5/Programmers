"""
def solution(a, b):
    day = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    aaa = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    summ = 0
    
    for i in range(0,a):
        summ += day[i] 
    summ += b 
     
    return aaa[summ % 7]
"""
#2022.11.13
import datetime

def solution(a, b):
    date = datetime.datetime(2016,a,b).strftime('%A')
    return date[:3].upper()
