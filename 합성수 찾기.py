def solution(n):
    answer = 0
    for num in range(1,n+1):
        for n in range(2,num):
            if num % n == 0:
                answer += 1
                break
    return answer
