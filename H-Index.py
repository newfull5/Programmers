'''
def solution(citations):
    citations.sort()
    answer = [0]
    
    for i in range(0, max(citations)):
        cnt = 0
        for j in range(0, len(citations)):
            if i <= citations[j]:
                cnt += 1
        if i <= cnt:
            answer.append(i)
            
    return max(answer)
'''
#2022.11.16
def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)
    
    for i in range(n, 0, -1):
        if citations[:i][-1] >= i and i > n-i:
            return i
    return 0
