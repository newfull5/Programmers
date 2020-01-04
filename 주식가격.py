def solution(price):
    answer = []
    
    for i in range(0, len(price)):
        for j in range(i+1, len(price)):
            if price[i] > price[j]:
                answer.append(j-i)
                break
            elif j == len(price)-1:
                answer.append(len(price)-i-1)
                break
    answer.append(0)
    
    return answer
                
