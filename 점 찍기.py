'''
def bisect(x,d):
    left = 0
    right = d
    mid = (left + right) // 2
    
    while left<=right:
        if x**2 + mid**2 == d**2:
            return [x, mid]
        
        if x**2 + mid**2 > d**2 and x**2 + (mid-1) < d**2:
            return [x, mid-1]
            
        if x**2 + mid**2 < d**2:
            left = mid+1
            mid = (left + right) // 2
            continue
            
        elif x**2 + mid**2 > d**2:
            right = mid
            mid = (left + right) // 2
            
def solution(k, d):
    lists = []
    for x in range(0, d+1, k):
        lists.append(bisect(x, d))
                
    answer = 0
    for x,y in lists:
        answer += (y // k)+1
        
    return answer
'''
import math

def solution(k, d):
    lists = []
    for x in range(0, d+1, k):
        lists.append([x, int((d**2 - x**2)**(1/2))])
        
    answer = 0
    for x,y in lists:
        answer += (y // k)+1
        
    return answer
