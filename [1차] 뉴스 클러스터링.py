"""
def solution(str1, str2):
    set1 = []
    set2 = []
    
    str1 = str1.upper()
    str2 = str2.upper()
    
    for i in range(len(str1)-1):
        if 65 <= ord(str1[i]) <= 90 and 65 <= ord(str1[i+1]) <= 90:
            set1.append(str1[i]+str1[i+1])

    for i in range(len(str2)-1):
        if 65 <= ord(str2[i]) <= 90 and 65 <= ord(str2[i+1]) <= 90:
            set2.append(str2[i]+str2[i+1])
            
    if not set1 and not set2:
        return 65536
            
    cnt = 0
    length = len(set1+set2)

    while set1 and set2:
        p = set1.pop()
        for st in set2:
            if p == st:
                cnt += 1
                set2.remove(st)
                break
                
    return int((cnt / (length - cnt)) * 65536)
"""
#2022.11.21
from collections import Counter

def solution(str1, str2):
    set1, set2 = [], []
    str1, str2 = str1.lower(), str2.lower()
    
    for i in range(1, len(str1)):
        if str1[i-1].isalpha() and str1[i].isalpha():
            set1.append(str1[i-1] + str1[i])
            
    for i in range(1, len(str2)):
        if str2[i-1].isalpha() and str2[i].isalpha():
            set2.append(str2[i-1] + str2[i])
    
    intersection = 0
    union = 0

    set1 = Counter(set1)
    set2 = Counter(set2)
    
    keys = set(set1.keys()) | set(set2.keys())

    if not keys:
        return 65536
    
    for v in keys:
        intersection += min(set1[v], set2[v])
        union += max(set1[v], set2[v])
        
    return int((intersection / union) * 65536)
