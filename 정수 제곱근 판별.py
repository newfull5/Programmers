def solution(n):

    for i in range(10000001):
        if i*i == n:
            return (i+1)*(i+1)

    return -1
