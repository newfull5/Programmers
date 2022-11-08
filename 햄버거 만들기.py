def solution(ingredient):
    answer = 0
    for i in range(len(ingredient)-3):
        if [1,2,3,1] == ingredient[i:i+4]:
            answer += 1
    return answer
