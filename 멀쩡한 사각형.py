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
