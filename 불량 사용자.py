'''
import re

def solution(user_id, banned_id):
    lists = []

    
    for a in banned_id:
        b = a.replace('*','[a-zA-Z0-9_]')
        q = re.compile(b)
        lists.append([k for k in user_id if q.search(k) and len(k) == len(a)])

    depth = len(lists)
    answer = []
    
    def DFS(visited, index):
        nonlocal answer
        nonlocal depth

        if index == depth:
            answer.append(tuple(sorted(visited)))
            return

        for string in lists[index]:
            if string not in visited:
                DFS(visited + [string], index+1)

        return

    DFS([],0)

    return len(set(answer))
'''
import re
from itertools import product

def solution(user_id, banned_id):
    answer = []
    visited = []
    
    for i in range(len(banned_id)):
        banned_id[i] = banned_id[i].replace('*','[a-zA-Z0-9]')
        banned_id[i] = '^'+banned_id[i]+'$'
    
    for ban in banned_id:
        id_list = []
        for user in user_id:
            if re.search(ban, user):
                id_list.append(re.search(ban, user).group())
        
        answer.append(id_list)
        
    for users in list(map(list, product(*answer))):
        users = sorted(users)
        
        if len(users) != len(set(users)):
            continue
            
        if users in visited:
            continue
            
        visited.append(users)
        
    return len(visited)
