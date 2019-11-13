def solution(heights):
    answer = []
    for i in range(0, len(heights)):
        if i == 0:
            answer.append(0)
        else:
            if max(heights[:i]) > heights[i]:
                for j in range(1, i+1):
                    if heights[:i][-j] > heights[i]:
                        answer.append(i-j+1)
                        break
            else:
                answer.append(0)
    return answer
