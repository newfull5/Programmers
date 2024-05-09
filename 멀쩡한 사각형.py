'''
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
def solution(w,h):
    width = w//gcd(w,h)
    height = h//gcd(w,h)
    
    a, b = max(width, height), min(width, height)
    
    if b+1 != a:
        unavail = b*2 + (a - (b+1))
    else:
        unavail = b*2
        
    return w*h - (unavail*(w//width))
'''
# 1:1 = 1/1
# 2:1 = 2/2
# 3:2 = 4/6
# 5:2 = 6/10
# 5:3 = 7/15
# 7:3 = 9/21
# a:b = a+b-1 / a*b

def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
def solution(w,h):
    width, height = w//gcd(w,h), h//gcd(w,h)
    return w*h-(w+h-gcd(w,h))
