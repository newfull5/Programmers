from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    
    gcd_a = arrayA.pop()
    for num in arrayA:
        gcd_a = gcd(num, gcd_a)
        
    gcd_b = arrayB.pop()
    for num in arrayB:
        gcd_b = gcd(num, gcd_b)
        
    for a in arrayA:
        if a % gcd_b == 0:
            break
    else:
        answer = max(gcd_b,answer)
        
    for b in arrayB:
        if b % gcd_a == 0:
            break
    else:
        answer = max(gcd_a,answer)
                    
    return answer
