from collections import Counter

def solution(array):
    crt = 0
    answer = 0
    dict = Counter(array)
    temp = sorted(dict.values())
    if len(dict.values()) > 1 and temp[-1] == temp[-2]:
        return -1
    
    for k,v in dict.items():
        if v > crt:
            crt = v
            answer = int(k)
            
    return answer
