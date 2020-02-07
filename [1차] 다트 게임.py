import re

def solution(dartResult):
    arr = []
    answer = 0
    p = re.compile("(\d+)([a-zA-Z])(\*|#)?")
    scores = p.findall(dartResult)

    for score in scores:
        if score[1] == 'S':
            arr.append(int(score[0])**1)
        if score[1] == 'D':
            arr.append(int(score[0])**2)
        if score[1] == 'T':
            arr.append(int(score[0])**3)

    for score in scores:
        if score[2] == '#':
            arr[scores.index(score)] = arr[scores.index(score)]*-1
        if score[2] == '*':
            arr[scores.index(score)] = arr[scores.index(score)]*2
            if scores.index(score) != 0:
                arr[scores.index(score)-1] = arr[scores.index(score)-1]*2
    return sum(arr)
