def solution(A,B):
    A.sort()
    B = sorted(B,reverse = True)
    temp = []
    for i in range(0, len(A)):
        temp.append(A[i]*B[i])
        
    return sum(temp)
