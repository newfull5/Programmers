from collections import Counter

def solution(want, number, discount):
    answer = 0
    want = {wan:num for wan,num in zip(want,number)}
    for i in range(len(discount)-9):
        if Counter(discount[i:i+10]) == want:
            answer += 1
    return answer
