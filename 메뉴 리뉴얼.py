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
