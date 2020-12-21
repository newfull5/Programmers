"""
#2020.10.13
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
    
def solution(n):
    return int(convert(n, base=3)[::-1], 3)
"""
#2020.12.21
def convert(n,base):
    
    nomi, denomi = divmod(n,base)

    if nomi == 0:
        return str(denomi)
    else:
        return convert(nomi, base) + str(denomi)
    
def solution(n):

    return int(convert(n,3)[::-1], 3)
