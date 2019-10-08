def solution(n):
    k = ""
    
    for i in range(n):
        if i % 2 == 0:
            k = k + "수"
        else:
            k = k + "박"
    return k
