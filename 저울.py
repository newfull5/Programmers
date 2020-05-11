def solution(weight):
    weight.sort()
    answer = 1
    
    for a in weight:
        if answer >= a:
            answer += a

    return answer
