'''
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(0, len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
'''
"""
#2020.07.13
#와 맙소사 톳씨하나 안틀리고 완전히 똑같다. 뭐지...
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(0, len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[-1]
"""
#2022.11.12
def solution(participant, completion):
    for p,c in zip(sorted(participant), sorted(completion)):
        if p != c:
            return p
    return list(set(participant) - set(completion)).pop()
