'''
def solution(A,B):
    A.sort()
    B = sorted(B,reverse = True)
    temp = []
    for i in range(0, len(A)):
        temp.append(A[i]*B[i])
        
    return sum(temp)
'''
#2020.03.04
def solution(A,B):
    A.sort()
    B.sort(reverse = True)

    temp = 0
    for i in range(0, len(A)):
        temp += A[i]*B[i]
    return temp
