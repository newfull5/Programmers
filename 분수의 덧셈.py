def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

def solution(denum1, num1, denum2, num2):
    num3 = num1 * num2
    denum3 = denum1 * num2 + denum2 * num1
    return [denum3 // gcd(num3,denum3), num3 // gcd(num3, denum3)]
