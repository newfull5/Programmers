def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def div_two(num):
    if num % 2 != 0:
        return num
    return div_two(num//2)

def div_five(num):
    if num % 5 != 0:
        return num
    return div_five(num//5)

def solution(a, b):
    b = b // gcd(a, b)
    b = div_five(div_two(b))
    
    if b == 1:
        return 1
    return 2
