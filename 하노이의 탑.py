def solution(n):
    answer = []
    
    def hanoi(start, middle, target, n):
        if n == 1:
            answer.append([start, target])
        else:
            hanoi(start, target, middle, n-1)
            hanoi(start, middle, target, 1)
            hanoi(middle, start, target, n-1)
            
    hanoi(1,2,3,n)
    
    return answer
