def solution(a, b, n):
    answer = 0
    while n >= a:
        print(n)
        quotient, n = divmod(n, a)
        answer += (quotient*b)
        n += (quotient*b)
        
    return answer
