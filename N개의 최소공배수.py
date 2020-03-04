'''
def gcd(a,b):
    a,b=max(a,b),min(a,b)
    while b > 0:
        a,b=b,a%b
    return a
def solution(arr):
    while len(arr) !=1:
        a=arr.pop()
        b=arr.pop()
        c=gcd(a,b)
        arr.insert(0,int(a*b/c))
    answer=arr[0]
    return answer
'''
#2020.03.04
def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b,a%b)

def chlthrhd(arr):
    if len(arr) == 1:
        return arr[0]
    a = arr.pop()
    b = arr.pop()
    chleorhd = gcd(a,b)
    arr.append(a*(b // chleorhd))
    return chlthrhd(arr)

def solution(arr):
    return chlthrhd(arr)
