'''
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
'''
# '실전에서 정규식을 사용할수 있을까?'하는 마음에 자료에 의존하지 않고 스스로 풀어보았다.
# 풀다보니 그냥 정규식을 공부하는 것이 나은것 같기도 하고 그렇다.
# 2020.02.26

def solution(dartResult):

    dartResult = list(dartResult)
    stack = []

    for i in range(0, len(dartResult)-1):
        if dartResult[i] == '1' and dartResult[i+1] == '0':
            stack.append('10')
            continue
        if stack != []:
            if stack[-1] == '10' and dartResult[i] == '0':
                continue
        stack.append(dartResult[i])
        
    stack.append(dartResult[-1])
    
    cnt = []
    for num in stack:
        if num.isnumeric():
            cnt.append(int(num))
        if num.isalpha():
            if num == 'D':
                cnt[-1] = cnt[-1]**2
            if num == 'T':
                cnt[-1] = cnt[-1]**3
        if num == '*':
            if len(cnt) == 1:
                cnt[-1] = cnt[-1]*2
            else:
                cnt[-1] = cnt[-1]*2
                cnt[-2] = cnt[-2]*2
        if num == '#':
            cnt[-1] = cnt[-1]*(-1)
            
    return sum(cnt)
