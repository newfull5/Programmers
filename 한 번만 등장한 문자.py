from collections import Counter

def solution(s):
    return ''.join(sorted([k for k,v in Counter(s).items() if v == 1]))
