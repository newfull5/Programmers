from collections import defaultdict

def solution(names, yearning, photos):
    diction = defaultdict(int)
    
    for name, yearning in zip(names, yearning):
        diction[name] = yearning
        
    result = []
    
    for photo in photos:
        result.append(sum([diction[v] for v in photo]))
        
    return result
