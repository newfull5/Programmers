def get_gcd(n, m):
    if m % n == 0:
        return n
    if n == 1:
        return 1
    
    return get_gcd(m%n, n)

def solution(n, m):
    gcd = get_gcd(n,m)
    return [gcd, m*n/gcd]
