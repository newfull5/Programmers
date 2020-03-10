def solution(n, s):
    if n > s:
        return [-1]
    
    a = [(s//n) for _ in range(n-(s-((s//n)*n)))]
    b = [((s//n)+1) for _ in range(s-((s//n)*n))]

    return a+b
