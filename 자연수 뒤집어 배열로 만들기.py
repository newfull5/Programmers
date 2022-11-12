"""
def solution(n):
    n = list(map(int,str(n)))
    answer = []
    
    for i in range(1, len(n)+1):
        answer.append(n[-i])

    return answer
"""
#2022.11.12
def solution(n):
    return [int(v) for v in str(n)[::-1]]
