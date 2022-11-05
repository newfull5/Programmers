def check_possible(a,b,c):
    return max([a,b,c]) < (sum([a,b,c])-max([a,b,c]))

def solution(sides):
    answer = 0
    a,b = min(sides), max(sides)
    
    for num in range(b-a-a, b+a):
        if check_possible(a,b,num):
            answer += 1
    return answer
