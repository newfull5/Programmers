'''
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
'''
#2022.11.24
def _jinbub(num, n):
    answer = ''
    while num > 0:
        num, remain = divmod(num, n)
        if remain >= 15 and n >= 15:
            answer += 'F'
        elif remain >= 14 and n >= 14:
            answer += 'E'
        elif remain >= 13 and n >= 13:
            answer += 'D'
        elif remain >= 12 and n >= 12:
            answer += 'C'
        elif remain >= 11 and n >= 11:
            answer += 'B'
        elif remain >= 10 and n >= 10:
            answer += 'A'
        else:
            answer += str(remain)
            
    return answer[::-1]
        

def solution(n, t, m, p):
    answer = ''
    span = '0'+''.join([_jinbub(v, n) for v in range(t*m+1)])
    
    for i, v in enumerate(span):
        if i % m == p-1:
            answer += v
        if len(answer) == t:
            return answer
