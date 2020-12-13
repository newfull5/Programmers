def solution(a, b):
    return sum(map(lambda x:x[0]*x[1], tuple(zip(a,b))))
 
