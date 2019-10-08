def solution(n):
    n = list(map(int,str(n)))
    answer = []
    
    for i in range(1, len(n)+1):
        answer.append(n[-i])

    return answer
