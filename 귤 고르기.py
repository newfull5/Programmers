from collections import Counter

def solution(k, tangerine):
    diction = Counter(tangerine)
    answer = 0
    for i, v in enumerate(sorted(diction.values(), reverse=True)):
        answer += v
        if answer >= k:
            return i+1
