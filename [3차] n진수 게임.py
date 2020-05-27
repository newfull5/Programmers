def Jinbup(number,n):
    T="0123456789ABCDEF"
    i,j=divmod(number,n)
    
    if i==0:
        return T[j]
    else:
        return Jinbup(i,n)+T[j]
    
def solution(n, t, m, p):
    string = ''
    answer = ''

    for i in range(100000):
        string += Jinbup(i,n)

    for i in range(p-1,100000,m):
        answer += string[i]
        if len(answer) == t:
            return answer
    
