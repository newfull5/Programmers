from itertools import combinations

def Isunique(lists,answer):
    for a in answer:
        if set(lists) & set(a) == set(a):
            return False
    return True

def solution(relation):
    stack = []
    answer = []
    relation = list(map(list,zip(*relation)))
    
    stack = sum([list(combinations(range(len(relation)),i)) for i in range(1,len(relation)+1)],[])
    
    for tup in stack:
        temp = []
        for a in tup:
            temp.append(relation[a])
        temp = list(map(tuple, zip(*temp)))
        if len(temp) == len(set(temp)):
            if Isunique(tup,answer):
                answer.append(tup)
                
    return len(answer)
