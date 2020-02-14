def solution(heights):
    answer = []
    
    for i in range(0, len(heights)):
        for j in range(i, -1, -1):
            if heights[i] < heights[j]:
                answer.append(j+1)
                break
            if j == 0:
                answer.append(0)
                break
                
    return answer
    
