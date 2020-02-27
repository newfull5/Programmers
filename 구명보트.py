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
