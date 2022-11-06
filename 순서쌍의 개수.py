def solution(n):
    answer = 0
    for v in range(1, n+1):
        if n % v == 0:
            answer += 1
    return answer
