def solution(a, b):
    mon = [31,29,31,30,31,30,31,31,30,31,30,31]
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    all_day = 0
    
    for i in range(0, a-1):
        all_day += mon[i]
        
    all_day += b-1
        
    return week[all_day % 7]
