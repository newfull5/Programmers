def solution(n):
    answer = []
    for i in range(1,n):
        temp = 0
        for j in range(i,n):
            temp += j
            if temp == n:
                answer.append(j-i)
            if temp > n:
                break
                
    return len(answer)+1
