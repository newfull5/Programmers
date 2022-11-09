"""
def solution(lottos, win_nums):
    least = set(lottos) & set(win_nums)
    
    r = 7 - len(least)
    if r == 7:
        r = 6
        
    l = 7 - (lottos.count(0)+ len(least))
    if l == 7:
        l = 6
        
    return [l, r]
"""
#2022.11.09

def solution(lottos, win_nums):
    answer = len(list(set(lottos) & set(win_nums)))
    answer = min(7-answer, 6)
    
    return [max(1, answer-lottos.count(0)), answer]
