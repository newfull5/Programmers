def solution(dots):
    x = [x for x,y in dots]
    y = [y for x,y in dots]
    
    return (max(x)-min(x)) * (max(y)-min(y))
