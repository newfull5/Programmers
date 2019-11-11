from collections import deque

def solution(strings, n):
    answer = []
    letter = []
    
    for word in strings:
        letter.append(word[n]) 
        
    deq = deque(zip(strings, letter))
    
    letter.sort()
    
    for i in range(0, len(strings)):
        for j in range(0, len(strings)):
            if letter[i] == deq[j][1]:
                answer.append(deq[j][0])
                
    return answer
