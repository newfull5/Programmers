'''
def solution(N, number):
    S = [{N}]
    for i in range(2, 9):
        lst = [int(str(N)*i)]
        for X_i in range(0, int(i / 2)):
            for x in S[X_i]:
                for y in S[i - X_i - 2]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1
'''
#2020.03.06
#이게 맞는 풀이인지 긴가민가 했는데, 이렇게  푸는게 맞는거였네
def make(arr1,arr2):
    answer = []
    arr1 = list(arr1)
    arr2 = list(arr2)
    for i in arr1:
        for j in arr2:
            answer.append(i+j)
            answer.append(i-j)
            answer.append(j-i)
            answer.append(i*j)
            answer.append(i/j)
            answer.append(j/i)
    answer = list(set(answer))
    answer.sort()
    for i in range(0, len(answer)):
        if answer[i] >= 1:
            answer = answer[i:]
            return set(answer)
        
def solution(N, number):
    n1 = {N}
    n2 = {10*N+N, 1, N+N}
    n3 = make(n1,n2)
    n4 = make(n1,n3) | make(n2,n2)
    n5 = make(n1,n4) | make(n2,n3)
    n6 = make(n1,n5) | make(n2,n4) | make(n3,n3)
    n7 = make(n1,n6) | make(n2,n5) | make(n3,n4)
    n8 = make(n1,n7) | make(n2,n6) | make(n3,n5)
    answer = [n1,n2,n3,n4,n5,n6,n7,n8]
    
    for arr in answer:
        if number in arr:
            return answer.index(arr)+1
    return -1
