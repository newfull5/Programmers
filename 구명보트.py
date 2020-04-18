'''
def solution(people, limit):
    people.sort()
    cnt = 0
    light = 0
    heavy = len(people)-1
    
    while heavy>light: 
        if people[light] + people[heavy] > limit:
            heavy -= 1
        else:
            cnt += 1
            heavy -= 1
            light += 1
            
    return len(people) - cnt
'''

#2020.04.18
def solution(people, limit):
    people.sort()
    a, b = 0, len(people)-1
    pair = 0

    while a < b:
        if people[a] + people[b] > limit:
            b -= 1
        else:
            pair += 1
            a += 1
            b -= 1
    return len(people)-pair

