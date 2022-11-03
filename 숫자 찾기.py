def solution(num, k):
    answer = str(num).find(str(k))
    if str(num).find(str(k)) != -1:
        return answer+1
    return answer
