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
