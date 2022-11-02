def solution(num, total):
    n = 0
    
    while True:
        answer = (n+num)*(n+num+1)/2 - n*(n+1)/2
        
        if answer == total:
            return [i+n+1 for i in range(num)]
        if answer > total:
            n -= 1
        if answer < total:
            n += 1
