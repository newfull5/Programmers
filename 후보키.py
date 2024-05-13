'''
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
'''
from itertools import combinations as c


def check_dup(answer, cols):
    for ans in answer:
        for n in ans:
            if n in cols:
                continue
            else:
                break
        else:
            return True
        
    return False

def check_valid_key(relation, key):
    sets = []
    
    for rel in relation:
        sets.append(''.join([rel[i] for i in key]))
        
    return len(set(sets)) == len(relation)


def solution(relation):
    answer = []
    
    col = [i for i in range(len(relation[0]))]
    
    for num_col in range(1, len(col)+1):
        for key in c(col, num_col):
            key = list(key)
            if check_dup(answer, key):
                continue
            
            if check_valid_key(relation, key):
                answer.append(key)
            
    return len(answer)
