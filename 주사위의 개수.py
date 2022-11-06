def solution(box, n):
    answer = 1
    for b in box:
        answer *= (b // n)
    return answer
