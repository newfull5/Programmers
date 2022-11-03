from collections import deque

def solution(A, B):
    A = deque(A)
    B = deque(B)

    for cnt in range(len(A)):
        if A == B:
            return cnt
        A.appendleft(A.pop())
        
    return -1
