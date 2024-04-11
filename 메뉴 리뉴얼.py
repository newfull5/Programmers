'''
from itertools import combinations as C

def solution(orders, course):    
    result = []

    for cour in course:
        arr = sum([list(map(lambda x: tuple(sorted(x)), C(string,cour))) for string in orders], [])
        cnt = 0
        answer = []
        for pair in set(arr):

            frequency = arr.count(pair)
            if cnt < frequency and frequency >= 2:
                answer = [pair]
                cnt = frequency

            elif cnt == frequency and frequency >= 2:
                answer.append(pair)

        result += [''.join(a) for a in answer]
        
    return sorted(result)
'''
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_candidates = Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)
