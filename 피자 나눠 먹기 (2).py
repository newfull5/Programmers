def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b, a%b)

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n == 4:
        return 2
    if n == 5:
        return 5
    if n == 6:
        return 1
    return n/gcd(n,6)
