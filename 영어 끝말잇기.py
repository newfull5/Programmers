'''
def solution(n, words):
    wrong = 0
    for i in range(0, len(words)-1):
        if words[i][-1] != words[i+1][0]:
            wrong = i+2
            break

    for i in range(0, len(words)-1):
        for j in range(i+1, len(words)):
            if words[i] == words[j]:
                wrong = j+1
                break
    
    if wrong == 0:
        return [0,0]
    if wrong%n == 0:
        return [n,wrong//n]
    else:
        return [wrong%n,(wrong//n)+1]
'''
'''
#2020.03.04
def solution(n, words):
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            if (i+1) % n == 0:
                return [n, (i // n)+1]
            return [(i+1) % n, (i // n)+1]
    return [0,0]
'''
#2022.11.14
import math

def solution(n, words):
    history = [words[0]]
    
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in history:
            people = n if (i+1) % n == 0 else (i+1)%n
            turn = math.ceil((i+1)/n)
            return [people, turn]
        history.append(words[i])
    return [0, 0]
