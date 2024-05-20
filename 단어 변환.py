"""
# 2020.4.14

def diffone(a,b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
        if cnt == 2:
            break    
    if cnt == 1:
        return True
    return False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    begin = [begin]
    answer = 0
    
    while words:
        for string in begin:
            temp = []
            for word in words:
                if diffone(string, word):
                    temp.append(word)
                    words.remove(word)
        answer += 1
        if target in temp:
            return answer
        begin = temp[:]
    return 0
"""

"""
# 2021.3.19

def solution(begin, target, words):
    
    answer = 51
    length = len(begin)
    
    def OneLetterDifferent(current,cnt,visited):
        nonlocal answer

        if current == target:
            answer = min(answer, cnt)
            return 

        for word in words:

            if word in visited:
                continue

            temp = 0

            for i in range(length):
                if current[i] != word[i]:
                    temp += 1

            else:
                if temp == 1:
                    OneLetterDifferent(word, cnt+1, visited + [word])
                    
    OneLetterDifferent(begin, 0, [])
    
    if answer == 51:
        return 0
    return answer
"""
'''
#2021.6.26
def solution(begin, target, words):
    def checkOneDiffent(begin,word):
        cnt = 0

        for i in range(len(begin)):
            if begin[i] != word[i]:
                cnt += 1

            if cnt >= 2:
                return False

        if cnt == 1:
            return True

        return False
    
    visited = []
    queue = [begin]

    cnt = 0

    while queue:
        cnt += 1
        for _ in range(len(queue)):

            begin = queue.pop(0)

            for word in words:

                if checkOneDiffent(begin, word) and word not in visited:
                    queue.append(word)
                    visited.append(word)

        if target in queue:
            return cnt

        words = list(set(words) - set(queue))
        
    return 0
'''
from collections import deque

def check_onediff(start, word):
    cnt = 0
    
    for i in range(len(start)):
        if start[i] != word[i]:
            cnt += 1
            
    if cnt == 1:
        return True
    return False


def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([[begin,0]])
    visited = [begin]
    
    while queue:        
        start, cnt = queue.popleft()
        if start == target:
            return cnt
        for word in words:
            if check_onediff(start, word) and (word not in visited):
                queue.append([word, cnt+1])
                visited.append(word)
        
        
