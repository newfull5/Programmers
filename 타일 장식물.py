def solution(N):
    answer = [1,1]
    for i in range(0,N-1):
        answer.append(answer[-1]+answer[-2])

    return ((answer[-1]+answer[-2])*2)
